from efl.elementary.button import Button


class ButtonArrays():
    def standard(self, ctx):
        return {
            "stackrow": [
                Button(ctx, text="History"), Button(ctx, text="About")
            ],
            "srcallbacks": [
                ctx.topButtonPressed, ctx.topButtonPressed
            ],
            "buttons": [
                [Button(ctx, text="CE"), Button(ctx, text="BKSP")],
                [Button(ctx, text="CLEAR"), Button(ctx, text="/"),
                 Button(ctx, text="*"), Button(ctx, text="-")],
                [Button(ctx, text="7"), Button(ctx, text="8"),
                 Button(ctx, text="9"), Button(ctx, text="+")],
                [Button(ctx, text="4"), Button(
                    ctx, text="5"), Button(ctx, text="6")],
                [Button(ctx, text="1"), Button(ctx, text="2"),
                 Button(ctx, text="3"), Button(ctx, text="=")],
                [Button(ctx, text="+/-"), Button(ctx, text="0"),
                 Button(ctx, text=".")]
            ],
            "callbacks": [
                [ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed]
            ],
            "positions": [
                [[0, 0, 2, 1], [2, 0, 2, 1]],
                [[0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1]],
                [[0, 2, 1, 1], [1, 2, 1, 1], [2, 2, 1, 1], [3, 2, 1, 2]],
                [[0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1]],
                [[0, 4, 1, 1], [1, 4, 1, 1], [2, 4, 1, 1], [3, 4, 1, 2]],
                [[0, 5, 1, 1], [1, 5, 1, 1], [2, 5, 1, 1]]
            ]
        }

    def scientific(self, ctx):
        return {
            "stackrow": [
                Button(ctx, text="DEG"), Button(
                    ctx, text="History"), Button(ctx, text="About")
            ],
            "srcallbacks": [
                ctx.setAngleMode, ctx.topButtonPressed, ctx.topButtonPressed
            ],
            "buttons": [
                [Button(ctx, text="CLEAR"), Button(
                    ctx, text="CE"), Button(ctx, text="BKSP")],
                [Button(ctx, text="e"), Button(ctx, text="pi"), Button(
                    ctx, text="("), Button(ctx, text=")"), Button(ctx, text="/")],
                [Button(ctx, text="inv"), Button(ctx, text="sin"), Button(
                    ctx, text="cos"), Button(ctx, text="tan"), Button(ctx, text="*")],
                [Button(ctx, text="sqrt"), Button(ctx, text="7"), Button(
                    ctx, text="8"), Button(ctx, text="9"), Button(ctx, text="-")],
                [Button(ctx, text="exp"), Button(ctx, text="4"), Button(
                    ctx, text="5"), Button(ctx, text="6"), Button(ctx, text="+")],
                [Button(ctx, text="log"), Button(ctx, text="1"), Button(
                    ctx, text="2"), Button(ctx, text="3"), Button(ctx, text="=")],
                [Button(ctx, text="ln"), Button(ctx, text="+/-"),
                 Button(ctx, text="0"), Button(ctx, text=".")]
            ],
            "callbacks": [
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed],
                [ctx.buttonPressed, ctx.buttonPressed,
                    ctx.buttonPressed, ctx.buttonPressed]
            ],
            "positions": [
                [[0, 0, 1, 1], [1, 0, 2, 1], [3, 0, 2, 1]],
                [[0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
                    [3, 1, 1, 1], [4, 1, 1, 1]],
                [[0, 2, 1, 1], [1, 2, 1, 1], [2, 2, 1, 1],
                    [3, 2, 1, 1], [4, 2, 1, 1]],
                [[0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1],
                    [3, 3, 1, 1], [4, 3, 1, 1]],
                [[0, 4, 1, 1], [1, 4, 1, 1], [2, 4, 1, 1],
                    [3, 4, 1, 1], [4, 4, 1, 1]],
                [[0, 5, 1, 1], [1, 5, 1, 1], [2, 5, 1, 1],
                    [3, 5, 1, 1], [4, 5, 1, 2]],
                [[0, 6, 1, 1], [1, 6, 1, 1], [2, 6, 1, 1], [3, 6, 1, 1]]
            ]
        }


if __name__ == "__main__":
    print("You seem lost, friend.\nPerhaps you should try running main.py instead?")
