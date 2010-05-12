###############################################################################
#Copyright (c) 2010, Ian Norris
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL IAN NORRIS BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################

###############################################################################
#Description: 	Script to allow installation of steam games from a second drive
#Usage: 		MakeSteamLink link
#					To create links
#			or
#				MakeSteamLink unlink
#					To remove all symbolic links from the target directory
###############################################################################

import os
import sys
from stat import *

#Import the library we need
import ctypes
kdll = ctypes.windll.LoadLibrary("kernel32.dll")

#File types to look for, make lower case!
file_types = [ ".ncf", ".gcf" ]

####################################################################
######################EDIT THESE PATHS!!!!##########################
####################################################################

#Source steam apps folder
steam_sources = [
	r"X:\Installs\Steam Apps"
]

#Target steam apps folder
steam_target = r"C:\Program Files (x86)\Steam\steamapps"

####################################################################
######################END OF EDITABLE BIT###########################
####################################################################

link_or_unlink = sys.argv[1]
link_or_unlink = link_or_unlink.lower()

def isLink( file ):
	if os.path.exists( file ):
		return (kdll.GetFileAttributesA( file ) & 1024) > 0
	return False

def die( msg ):
	print >>sys.stderr, msg
	exit(1)

def MakeLinkFile( target, source ):
	result = kdll.CreateSymbolicLinkA( source, target, 0)
	if( result == 0 ):
		die( target + " - " + ctypes.FormatError() )

def MakeLinkDir( target, source ):
	kdll.CreateSymbolicLinkA( source, target, 1)
	
def RemoveLink( file ):
	if isLink( file ):
		if os.path.isdir( file ):
			print "Removing directory link to " + file
			kdll.RemoveDirectoryA( file )
		else:
			print "Removing file link to " + file
			kdll.DeleteFileA( file )

#For all files in the root steam apps dir
def LinkDirectories( source_path, target_path, recurse ):
	try:
		dir_contents = os.listdir(source_path)
		for file in dir_contents:
			file_source_path = source_path + '\\' + file
			file_target_path = target_path + '\\' + file
			
			#Don't mess with existing symlinks
			if not isLink(file_target_path):
				#If it's a file
				if os.path.isfile(file_source_path):
					# If the extension matches our list...
					if(os.path.splitext(file_source_path)[1].lower() in file_types):
						# If the target file does NOT already exist
						if( not os.path.exists( file_target_path ) ):
							#Make a symbolic file link
							MakeLinkFile( file_source_path, file_target_path )
				#If it's a directory
				elif( os.path.isdir(file_target_path) ):
					#And we haven't hit our recursion limit
					if( recurse > 0 ):
						#Make a link
						LinkDirectories( file_source_path, file_target_path, recurse-1 )
				#If the source directory exists and the target is not a link
				elif( os.path.isdir(file_source_path) ):
					#Recurse
					MakeLinkDir( file_source_path, file_target_path )
			else:
				print "Skipping " + file_target_path + ", it was already a link"
	except:
		pass

def UnlinkDirectories( target_path ):
	try:
		dir_contents = os.listdir(target_path)
		for file in dir_contents:
			file_path = target_path + '\\' + file
			if isLink(file_path):
				RemoveLink( file_path )
			elif os.path.isdir(file_path):
				UnlinkDirectories( file_path )
	except:
		pass
	
#Now run script	for files
if link_or_unlink == "unlink":
	print "Removing all symbolic links from the target steam folder"
	UnlinkDirectories( steam_target )
else:
	print "Making symbolic links"
	for source in steam_sources:
		LinkDirectories( source, steam_target, 2 )

print "All done!"