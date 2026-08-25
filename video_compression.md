# 720p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 22 -b:v 0 -maxrate 6M -bufsize 12M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 720p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 22 -b:v 0 -maxrate 8M -bufsize 16M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 1080p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 21 -b:v 0 -maxrate 12M -bufsize 24M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 1080p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 21 -b:v 0 -maxrate 16M -bufsize 32M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 1440p 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 20 -b:v 0 -maxrate 22M -bufsize 44M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 1440p 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 20 -b:v 0 -maxrate 32M -bufsize 64M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 4K 30fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 19 -b:v 0 -maxrate 50M -bufsize 100M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv
# 4K 60fps
ffmpeg -i input.mkv -c:v hevc_nvenc -preset p7 -tune hq -rc vbr -cq 19 -b:v 0 -maxrate 65M -bufsize 130M -multipass fullres -spatial-aq 1 -aq-strength 8 -temporal-aq 1 -rc-lookahead 32 -bf 4 -b_ref_mode middle -c:a copy output.mkv