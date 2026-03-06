# 13. In your ed-tech platform, determine video streaming quality. Write a nested if/else block: First check if is_premium_user is True. If so, check if bandwidth_mbps >= 10; if true, quality is "4K", else "1080p". If not a premium user, quality is "720p" regardless of bandwidth.

is_premium_user = bool(int(input('Enter 0 for false and 1 for true: ')))
quality = ''

if is_premium_user:
    bandwidth_mbps = int(input('Enter your bandwidth in mbps: '))
    if bandwidth_mbps >= 10:
        quality = '4K'
    else:
        quality = '1080p'
else:
    quality = '720p'

print(quality)