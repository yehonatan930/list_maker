import os
import re


sl = ['D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E100-E102.480p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E103-E104.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E105.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E106.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E107-E108.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E109-E110.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E111-E112.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E113-E114.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E115.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E116-E117.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E118-E119.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E120.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E92.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E93-E95.1080p.mkv', 'D:\\כרגע\\One Piece [tvdb4-81797]\\Arc 12 - Arabasta\\One.Piece.E96-E98.1080p.mkv']
sl.sort(key=lambda x: int(re.search(r'\d+', os.path.basename(x)).group()))
print(sl)

# for x in sl:
#     print(int(re.search(r'\d+', os.path.basename(x)).group()))