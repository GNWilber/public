# 720p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 4M -maxrate 6M -bufsize 8M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 720p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 6M -maxrate 8M -bufsize 12M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 1080p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 8M -maxrate 12M -bufsize 16M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 1080p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 12M -maxrate 16M -bufsize 24M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 1440p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 16M -maxrate 22M -bufsize 32M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 1440p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 24M -maxrate 32M -bufsize 48M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 4K 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 35M -maxrate 50M -bufsize 70M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv

# 4K 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p6 -rc vbr -b:v 50M -maxrate 65M -bufsize 100M -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 3 -c:a copy output.mkv