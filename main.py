from maps.GakushokuSample import GakushokuSample
from maps.takeda import takeda
from maps.KamiokaOsusume import KamiokaOsusume
from maps.OmuraOsusume import OmuraOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [KamiokaOsusume(),
        takeda(),
        OmuraOsusume()] 


for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
