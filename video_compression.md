# 1080p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 28 -b:v 4M -maxrate 6M -c:a copy output.mkv

# 1080p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 26 -b:v 6M -maxrate 8M -c:a copy output.mkv

# 4K 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 24 -b:v 15M -maxrate 20M -c:a copy output.mkv

# 4K 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 22 -b:v 25M -maxrate 30M -c:a copy output.mkv