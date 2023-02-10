import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
        totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae 
        dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut 
        fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque 
        porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed 
        quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat 
        voluptatem. Ut enim ad minima veniam, quis nostrum[d] exercitationem ullam corporis suscipit 
        laboriosam, nisi ut aliquid ex ea commodi consequatur
        """, classes="text-lg")
        return wp