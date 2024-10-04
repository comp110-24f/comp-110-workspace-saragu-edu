"""For qc04, coordinates file"""

__author__ = "730758554"


def get_coords(xs: str, ys: str) -> None:
    iy = 0
    ix = 0
    # variables for searching the index of x and y
    while ix < len(xs):
        # searches though index x
        iy = 0
        print("(" + xs[ix] + "," + ys[iy] + ")")
        while iy < len(ys) - 1:
            # searches index for y
            iy = iy + 1
            print("(" + xs[ix] + "," + ys[iy] + ")")
        ix = ix + 1
