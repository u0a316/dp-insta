# dp-insta

# luisadha/drawercli: This cli app supports using termuxlauncher as your primary launcher for Android phones, interactively and easily install. That's simply the Termuxlauncher Add-on built with fzf🚀

[![Maintained-Yes](https://camo.githubusercontent.com/4ae374aff8abab3cb4e5774a4bd6094c3a9b01d52bb3ea6b838b37a39e5bd62f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d61696e7461696e65642533462d7965732d677265656e2e737667)](https://img.shields.io/badge/Maintained%3F-yes-green.svg)[![Fetch-license](https://camo.githubusercontent.com/cb6d6ce0b300f990de5ac62ee6624fca10fa323297e5e8c3ca62b4252376f584/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6c756973616468612f647261776572636c692e737667)](https://img.shields.io/github/license/luisadha/drawercli.svg)[![Total-downloads](https://camo.githubusercontent.com/7f4c22c38e32cfaff42b7bef72d1e3f5c98773dea55afcd8c0809b4ed9386408/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6c756973616468612f647261776572636c692f746f74616c2e737667)](https://img.shields.io/github/downloads/luisadha/drawercli/total.svg)[![Stargazer](https://camo.githubusercontent.com/4b8f8ae9ef5417bd8fea42cc66ab3547249953f8984a6adc3009e539ba49510e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6c756973616468612f647261776572636c692e737667)](https://img.shields.io/github/stars/luisadha/drawercli.svg)[![Fork-totals](https://camo.githubusercontent.com/2b433a880d44d36dc6444811d90302eec8535dfc2dc7eabcbcd83a307404f539/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6c756973616468612f647261776572636c692e737667)](https://img.shields.io/github/forks/luisadha/drawercli.svg)[![Watcher-totals](https://camo.githubusercontent.com/224a4340d2968b8a1f18119f913f59eef8937d2aa707817d7fa81310dcbecf4a/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f77617463686572732f6c756973616468612f647261776572636c692e737667)](https://img.shields.io/github/watchers/luisadha/drawercli.svg)

# Drawercli-lightwieght for Termux

[](#drawercli-lightwieght-for-termux)

Application drawer in the terminal. Requires the Termuxlauncher library or app and Termux installed on the device.

**Also find drawercli on alrc-termux plugin.**

-   Interactive by scrolling the screen to select apps and typing to find favorite apps (this parts has been improved on new update).
    
-   Updated app list in Termuxlauncher.
    
-   Display frequently opened apps.
    
-   Makes app suggestions to open with a specified number.
    
-   Calculate total user applications
    
-   Support touchscreen
    
-   Can be installed in ~/.shortcuts to run via Termux:widget
    
-   Can be installed on ztmexluis or luis-toolbox.sh
    

Note

Without Termuxlauncher & Termux this tool won't work.

#### A. Download and install these apk's

[](#a-download-and-install-these-apks)

-   Termuxlauncher apk's [Check this!](https://github.com/amsitlab/termuxlauncher/releases)
-   Termux:widget (optional) [Find on Play store](https://play.google.com/store/apps/details?id=com.termux.widget)

-   `input` keyevent (is in /system/bin make sure it is part of the $PATH variable) (**Optional**)
-   git, curl, fzf, coreutils, sed, grep and which.
-   termux-setup-storage

## Install with Bash Package Manager ([bpkg](https://bpkg.sh/bpkg/))

[](#install-with-bash-package-manager-bpkg)

bpkg install -g luisadha/drawercli

-   Install with Make

-   Install with Nix-build

-   general (i.e.: termux)

rm -f ${PREFIX}/bin/drawercli

-   nix-on-droid

nix-env -e drawercli
nix-env --rollback

-   gnumake

Try our custom configurations, Termux config is stored in ~/.termux/termux.properties

extra-keys-style = none
extra-keys = \[\[{key: "drawercli \\n", popup: KEYBOARD, display: drawercli}\]\]

drawercli -S 4 | -u

 Command-line-based app drawer to display a list of all user-installed apps on the device and many other features.

drawercli requires the termuxlauncher to be installed and used at least once to use this tool.

Available options:

-S NUMBER                To display app recommendations to open, recommendations will be displayed according to the given number.
-c, --clear-history      To clear the history of opened app activities.
-r                       To refresh the list of apps, newly installed apps will be displayed after the refresh.
-s, --skip               Does nothing, literally opens Termux itself.
-u                       To display the most frequently used apps.
-w, --see-wallpaper      To view the wallpaper or open the current-wallpaper app.
-h, --help               To display this help message.

| Platform | Status |
| --- | --- |
| Termux | ✅ |
| Nix-on-droid | ✅ |
| Acode Terminal Plugin | ❌ |

Issues related to nix-on-droid, Try clearing this duplicate package garbage fix

@luisadha

@zaedstudioshpkentang

-   Creator of Termuxlauncher and termux for creating great apps
-   pick tools
-   fzf tools
-   bpkg (bash package manager)