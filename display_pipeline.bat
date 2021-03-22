IF exist C:\gstreamer\1.0\msvc_x86_64\bin (^
C:\gstreamer\1.0\msvc_x86_64\bin\gst-launch-1.0 -v udpsrc address=192.168.1.195 port=8000 caps="application/x-rtp, media=video, payload=96, clock-rate=90000, encoding-name=H264" ! rtph264depay ! queue ! decodebin ! videorate ! "video/x-raw, framerate=120/1" ! fpsdisplaysink sync=false -e^
) else (^
    IF exist D:\gstreamer\1.0\msvc_x86_64\bin (^
    D:\gstreamer\1.0\msvc_x86_64\bin\gst-launch-1.0 -v udpsrc address=192.168.1.195 port=8000 caps="application/x-rtp, media=video, payload=96, clock-rate=90000, encoding-name=H264" ! rtph264depay ! queue ! decodebin ! videorate ! "video/x-raw, framerate=120/1" ! fpsdisplaysink sync=false -e^
    ) else (^
    ECHO "Check your path for GStreamer")^
)