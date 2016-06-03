{
    "targets": [
        {
            "target_name": "usonic",
            "sources": [
                "src/clock.cc",
                "<!(node -p \"require('path').relative(__dirname, require.resolve('mmm-gpio').replace('lib/gpio.js', 'src/gpio.cc'))\")",
                "src/node_usonic.cc"
            ],
            "include_dirs" : [
                "<!(node -e \"require('nan')\")",
                "<!(node -p \"require.resolve('mmm-gpio').replace('lib/gpio.js', 'src')\")"
            ]
        }
    ]
}
