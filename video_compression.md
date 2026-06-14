# 1080p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 28 -b:v 6M -maxrate 9M -c:a copy output.mkv

# 1080p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 26 -b:v 9M -maxrate 12M -c:a copy output.mkv

# 4K 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 24 -b:v 23M -maxrate 30M -c:a copy output.mkv

# 4K 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -rc vbr -cq 22 -b:v 38M -maxrate 45M -c:a copy output.mkv