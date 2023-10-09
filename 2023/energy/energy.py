from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        objs = []
        for i in range(2, 9):
            objs.append(Circle(radius=i, color=BLUE))

        circles = VGroup(*objs)

        t = Text("אנרגיה")
        self.play(DrawBorderThenFill(circles), Write(t))
        self.wait(3)

        self.play(t.animate.shift(UP*3), FadeOut(circles))

        self.wait(3)

        light = Text("אנרגיית אור", color=BLUE)
        heat = Text("אנרגיית חום", color=RED)
        electricity = Text("אנרגיה חשמלית", color=YELLOW)
        muchmore = Text("ועוד הרבה מאוד!")
        muchmore.shift(DOWN*4)
        self.play(Write(light, run_time=0.5), light.animate.shift(UP+RIGHT))
        self.wait(0.25)
        self.play(Write(heat, run_time=0.5), heat.animate.shift(DOWN+LEFT))
        self.wait(0.25)
        self.play(Write(electricity, run_time=0.5), electricity.animate.shift(DOWN*2+RIGHT*2))
        self.wait(2)
        self.play(FadeOut(light, heat, electricity))

        nuhuh = Text("לא לא לא!")
        self.play(Write(nuhuh))
        self.wait()
        self.play(FadeOut(nuhuh))
        self.wait(2)

        haavara = Text("העברת אנרגיה", color=RED)
        hamara = Text("המרת אנרגיה", color=BLUE)
        hamara.shift(UP)
        haavara.shift(DOWN)
        line = Line(LEFT*3, RIGHT*3)
        self.play(Write(line), Write(hamara))
        self.wait(0.5)
        self.play(Write(haavara))
        self.wait()
        self.play(FadeOut(line, haavara, hamara, t))

class Difference(Scene):
    def construct(self):
        d = Text("אז, מה ההבדל בין השניים?")
        self.play(Write(d))
        self.play(d.animate.shift(3*UP))

        hamara = Text("המרת אנרגיה")
        hamara.shift(2*UP)
        haavara = Text("העברת אנרגיה")
        haavara.shift(2*UP)
        self.play(Write(hamara))

        self.wait(1)

        one = Text("אנרגיה חשמלית", color=RED)
        two = Text("אנרגיית אור", color=BLUE)
        self.play(Write(one))
        self.wait(0.5)
        self.play(ReplacementTransform(one, two))

        self.play(FadeOut(two, hamara))
        self.play(Write(haavara))

        one = Rectangle(color=RED, fill_opacity=1)
        one.shift(3*LEFT)
        energy = Text("אנרגיית חום")
        energy.move_to(one)

        two = Rectangle(color=BLUE, fill_opacity=1)
        two.shift(3*RIGHT)

        arrow = Line(one.get_center(), two.get_center())
        
        self.play(DrawBorderThenFill(one), DrawBorderThenFill(two), Write(energy))
        self.wait(0.25)
        self.play(Write(arrow))
        self.play(energy.animate(run_time=2).move_to(two))
        self.play(Unwrite(arrow))

        self.play(FadeOut(one), FadeOut(two), FadeOut(arrow), FadeOut(d), FadeOut(haavara), FadeOut(energy))

class Cradle(Scene):
    def construct(self):
        objs = []

        for i in range(5):
            objs.append(Circle(radius=0.5, color=GRAY).shift((-2+i)*RIGHT))

        cradle = VGroup(*objs)
        cradle.shift(DOWN)

        c = Text("העריסה של ניוטון")
        self.play(Write(c))
        self.play(c.animate.shift(3*UP))
        self.play(Write(cradle))
        self.wait(2)

        self.play(objs[0].animate(run_time=0.5).shift(2*LEFT+1*UP))
        self.play(objs[0].animate(run_time=0.5).shift(2*RIGHT+1*DOWN))
        self.wait(1)
        a = Arrow(objs[0].get_center(), objs[-1].get_center())
        self.play(Write(a))
        self.wait(1)
        self.play(FadeOut(a))
        self.play(objs[-1].animate(run_time=0.5).shift(2*RIGHT+1*UP))
        self.play(objs[-1].animate(run_time=0.5).shift(2*LEFT+1*DOWN))
        anims = []
        self.play(FadeOut(cradle))
        interesting = Text("אפקט מעניין")
        self.play(Write(interesting))
        self.play(interesting.animate.shift(2*UP))
        self.play(Write(cradle))
        self.play(objs[0].animate(run_time=0.5).shift(2*LEFT+1*UP), objs[1].animate(run_time=0.5).shift(2*LEFT+1*UP))
        self.play(objs[0].animate(run_time=0.5).shift(2*RIGHT+1*DOWN), objs[1].animate(run_time=0.5).shift(2*RIGHT+1*DOWN))
        self.wait(2)
        self.play(objs[-1].animate(run_time=0.5).shift(2*RIGHT+1*UP), objs[-2].animate(run_time=0.5).shift(2*RIGHT+1*UP))
        self.play(objs[-1].animate(run_time=0.5).shift(2*LEFT+1*DOWN), objs[-2].animate(run_time=0.5).shift(2*LEFT+1*DOWN))
        itsreal = Text("זה אמיתי, תנסו את זה בבית!")
        itsreal.shift(DOWN*3)
        self.play(Write(itsreal))
        self.wait(2)
        self.play(FadeOut(interesting), FadeOut(itsreal), FadeOut(cradle))
        youthink = Text("מה אתם חושבים שזה?")
        self.play(Write(youthink))
        secs = Text("אל תדאגו, אני אתן זמן!")
        secs.scale(0.75)
        secs.shift(DOWN)
        self.play(Write(secs))
        self.wait(3)
        self.play(FadeOut(secs, run_time=2))
        haavara = Text("זוהי העברת אנרגיה!")
        self.play(Transform(youthink, haavara))
        why = Text("אנרגיית התנועה של כדור אחד עובר לאחרים")
        why.shift(DOWN)
        self.play(Write(why))
        self.wait(5)
        anims = []
        anims.append(FadeOut(why))
        anims.append(FadeOut(youthink))
        anims.append(FadeOut(c))
        self.play(*anims)

class TVScreen(Scene):
    def construct(self):
        rect = Rectangle(width=8, height=4)
        line = Line(RIGHT*2+DOWN*2, RIGHT*3+DOWN*3)
        line2 = Line(LEFT*2+DOWN*2, LEFT*3+DOWN*3)

        tv = VGroup(rect, line, line2)
        text = Text("מסך טלוויזיה")
        chan_location = 3*RIGHT+DOWN
        channel = Text("12")
        channel.shift(chan_location)
        channel.scale(0.75)

        self.play(DrawBorderThenFill(tv), Write(text))
        self.wait()
        self.play(Unwrite(text))

        axes = Axes(x_range=[-1, 10], y_range=[-1, 10])
        power_cord = axes.plot(lambda x: np.sin(x), x_range=[1, PI*1.44], color=WHITE)
        power_cord.shift(LEFT*4+UP*2)
        self.play(Write(power_cord))
        self.wait()
        self.play(rect.animate.set_fill(opacity=1, color=color_gradient([RED, GREEN, BLUE], length_of_output=10)), FadeIn(channel))
        self.wait()
        what = Text("מה אתם חושבים שזה?")
        time = Text("יש זמן...").shift(DOWN).scale(0.75)
        self.play(Write(what), Write(time), Transform(channel, Text("84").scale(0.75).shift(chan_location)), rect.animate.set_fill(opacity=0))
        self.wait(3)
        self.play(Unwrite(channel, run_time=1))
        self.wait()
        hamara = Text("זו המרת אנרגיה!")
        why = Text("אנרגיה חשמלית הופכת לאנרגיית אור").shift(DOWN).scale(0.75)
        self.play(ReplacementTransform(what, hamara), ReplacementTransform(time, why))
        self.wait(5)
        self.play(FadeOut(hamara, why, tv, power_cord))

class Preintro(Scene):
    def construct(self):
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo = ManimBanner()
        logo.move_to(ORIGIN)
        logo.scale(0.7)
        text = Text("תוכנת עם מנים")
        text.shift(DOWN*2)
        self.play(logo.create())
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(logo), FadeOut(text))

        madeby = Text('נוצר על ידי')
        madeby.shift(UP*3)
        ilay = Text('עילאי לוי')
        objs = []
        objs.append(Circle(radius=2, fill_opacity=0.5, color=RED).shift(LEFT))
        objs.append(Circle(radius=2, fill_opacity=0.5, color=GREEN))
        objs.append(Circle(radius=2, fill_opacity=0.5, color=BLUE).shift(RIGHT))
        circles = VGroup(*objs)
        self.play(Write(madeby))
        self.play(DrawBorderThenFill(circles), Write(ilay))
        self.wait(2)
        self.play(FadeOut(circles), FadeOut(ilay), FadeOut(madeby))

class Thanks(Scene):
    def construct(self):
        thanks = Text("תודה רבה!")
        self.play(Write(thanks))
        self.play(thanks.animate.shift(3*UP))
        self.wait()
        yt_rect = RoundedRectangle(color=RED, fill_opacity=1, width=3)
        yt_play = Triangle(fill_opacity=1, color=WHITE)
        yt_play.rotate(-TAU/4)
        yt_play.scale(0.5)
        yt_play.move_to(yt_rect)
        yt_url = Text("@teesh3rt")
        yt_url.next_to(yt_rect, DOWN)
        yt = VGroup(yt_rect, yt_play, yt_url, fill_opacity=1)
        self.play(Write(yt))
        self.wait()
        self.play(FadeOut(yt))
        self.wait(2)
        math = Text("מתמטיקה", color=RED).shift(UP)
        science = Text("מדעים", color=BLUE)
        computers = Text("מחשבים", color=YELLOW).shift(DOWN)
        self.play(Write(math))
        self.play(Write(science))
        self.play(Write(computers))
        self.wait()
        self.play(FadeOut(math, science, computers))
        co = Text("תבדקו אותו!")
        self.play(Write(co))
        self.wait()
        self.play(Transform(co, Text("ביי ביי!")))
        self.wait()
        self.play(FadeOut(co, thanks))