solutions = [
  { "name"        : "src",
    "url"         : "https://github.com/Unpublished/android_external_gello-env.git@refs/remotes/origin/m52",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "safesync_url": "",
    "managed"     : False,
    "custom_deps" : {
        "src/swe/browser" : "https://github.com/Unpublished/android_packages_apps_Gello.git@refs/remotes/origin/cm-13.0"
    }
  },
]
target_os = ["android"]
