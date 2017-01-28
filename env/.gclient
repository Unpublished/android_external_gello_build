solutions = [
  { "name"        : "src",
    "url"         : "git://codeaurora.org/quic/chrome4sdp/chromium/src.git@refs/remotes/origin/m57",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "safesync_url": "",
    "managed"     : False,
    "custom_deps" : {
        "src/swe/channels/custom" : "https://github.com/Unpublished/swe_channel_custom.git"
    }
  },
]
target_os = ["android"]
