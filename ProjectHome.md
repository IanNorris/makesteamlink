If you have a small boot drive like an SSD, not being able to run Steam games from multiple drives can be a real pain. This script helps to alleviate this by creating symbolic links between multiple steam 'sources' and your main steam install directory.

Steam will automatically detect the games from these links and update the version in the relevant directory. New games will get downloaded to your main steam folder.

The script also includes an 'unlink' command that removes all existing symbolic links.

The script requires Python 2.6