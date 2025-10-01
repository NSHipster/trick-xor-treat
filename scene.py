from manim import *
from manim_voiceover_fixed import VoiceoverScene
from manim_voiceover_fixed.services.elevenlabs import ElevenLabsService
from contextlib import contextmanager


class TrickXORTreat(VoiceoverScene):
    # @contextmanager
    # def voiceover(self, text, **kwargs):
    #     """Stub for self.voiceover to avoid API calls during development."""
    #     yield

    def construct(self):
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Liam", model="eleven_v3", transcription_model=None
            )
        )

        title = Text("Trick XOR Treat: A Halloween Logic Tale", weight=BOLD).scale(0.7)
        title.to_edge(UP, buff=0.6)
        subtitle = Text("A 3blue1brown-style explainer by NSHipster", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.2)

        # Credit at the bottom
        credit = Text("Inspired by a Tweet by @38mo1", font_size=28, color=GRAY)
        credit.to_edge(DOWN, buff=0.5)

        with self.voiceover(
            text="""Every kid knows the phrase, [kid sing-songy] "Trick or treat!" 
                    But have you ever stopped to wonder —
                    what kind of _"or"_ is that, exactly?"""
        ):
            self.play(Write(title), run_time=1.2)
            self.play(FadeIn(subtitle, shift=UP), run_time=0.8)
            self.play(FadeIn(credit, shift=UP), run_time=0.8)
            self.wait()

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(credit), run_time=0.6)
        self.remove(title)
        self.remove(subtitle)
        panel = self.create_panel("OR", scale_factor=1.35)
        panel.move_to(ORIGIN)
        legend = self.create_legend().next_to(panel, RIGHT, buff=0.6)

        self.play(FadeIn(panel, scale=1.05), FadeIn(legend), run_time=1.0)

        with self.voiceover(
            text="""Let's start with the obvious interpretation:
                    
                    Two circles—two children.
                    Orange means treats, gray means tricks.
                    This is inclusive OR: 
                    If any child knocks, everyone gets candy.
                    Only an empty porch gets tricks."""
        ):
            self.wait()

        self.wait(0.25)

        with self.voiceover(
            text="""[quickly] [chuckles] Is this how Venn diagrams work? Not at all! 
                    But hey, it's Halloween—logic gets to wear a costume, too."""
        ):
            self.play(FadeOut(legend, shift=UP), run_time=0.5)
            self.wait()

        panel = self.transition_panel(
            panel, self.create_panel("AND", scale_factor=1.35)
        )
        with self.voiceover(
            text="""[title] Trick AND Treat

                    Both children must show up together, or nobody gets treats.
                    [sarcastic] One lonely kid?
                    Sorry, that's a trick."""
        ):
            self.wait()

        panel = self.transition_panel(
            panel, self.create_panel("XOR", scale_factor=1.35)
        )
        with self.voiceover(
            text="""[title] Trick XOR Treat

                     This house rewards exactly one visitor.
                     Too few or too many, and everyone gets tricked."""
        ):
            self.wait()

        self.play(FadeOut(panel, run_time=0.6))

        non_negated_ops = ["OR", "AND", "XOR"]
        non_negated_panels = [self.create_panel(op) for op in non_negated_ops]
        non_negated_gallery = (
            VGroup(*non_negated_panels).arrange(RIGHT, buff=0.5).scale(0.6)
        )
        self.play(
            LaggedStart(
                *[FadeIn(p, shift=UP) for p in non_negated_gallery], lag_ratio=0.1
            ),
            run_time=1.6,
        )

        with self.voiceover(
            text="""These three behaviors cover most houses on the block. 
                    But De Morgan's laws hint at something more... 
                    a theoretical complement to each.
                    A spooky, inverted reflection."""
        ):
            self.wait()

        self.wait(0.5)

        with self.voiceover(
            text="""[spooky] What cursed operations lurk in the penumbra of reason?
                    Let's face our fears and venture into the dark."""
        ):
            # Shift panels up to make room for question marks
            self.play(non_negated_gallery.animate.shift(UP * 0.8), run_time=0.8)

            # Add dashed lines and question marks to suggest the negated forms
            dashed_lines = VGroup()
            question_marks = VGroup()

            for i, panel in enumerate(non_negated_gallery):
                # Create dashed line pointing down from each panel
                start_point = panel.get_bottom() + DOWN * 0.3
                end_point = start_point + DOWN * 1.5
                dashed_line = DashedLine(
                    start_point, end_point, color=WHITE, dash_length=0.1
                )
                dashed_lines.add(dashed_line)

                # Create question mark at the end of each line
                question_mark = Text("?", font_size=48, color=WHITE).move_to(
                    end_point + DOWN * 0.8
                )
                question_marks.add(question_mark)

            self.play(
                LaggedStart(*[Create(line) for line in dashed_lines], lag_ratio=0.2),
                run_time=1.0,
            )
            self.play(
                LaggedStart(
                    *[FadeIn(q, scale=0.5) for q in question_marks], lag_ratio=0.2
                ),
                run_time=0.8,
            )
            self.wait()

        self.play(
            FadeOut(dashed_lines),
            FadeOut(question_marks),
            FadeOut(non_negated_gallery),
            run_time=0.8,
        )

        panel = self.create_panel("NOR", scale_factor=1.35)
        panel.move_to(ORIGIN)
        self.play(FadeIn(panel, scale=1.05), run_time=0.8)
        with self.voiceover(
            text="""[title] Trick NOR Treat: the Halloween hater.

                    This neighbor only gives treats when nobody visits.
                    [quick laugh] The only winning move is not to play."""
        ):
            self.wait()

        panel = self.transition_panel(
            panel, self.create_panel("NAND", scale_factor=1.35)
        )
        with self.voiceover(
            text="""[title] Trick NAND Treat: NOT-AND—the reverse psychology neighbor.

                    This house gives treats to everyone... except pairs.
                    Come alone? Treats. 
                    Don't come at all? ...[chuckles] Also Treats. 
                    Come together? [mischievous] That's the only way to get tricked."""
        ):
            self.wait()

        panel = self.transition_panel(
            panel, self.create_panel("XNOR", scale_factor=1.35)
        )
        with self.voiceover(
            text="""[title] Trick XNOR Treat: the conformity enforcer—XOR inverted.

                    This neighbor rewards matching behavior.
                    Both kids visit, or both stay home? Treats.
                    Just one kid? [judgmental] That's a trick."""
        ):
            self.wait()

        self.play(FadeOut(panel, run_time=0.6))

        self.wait(0.5)

        gallery = self.create_gallery()
        self.play(
            LaggedStart(*[FadeIn(p, shift=UP) for p in gallery], lag_ratio=0.1),
            run_time=1.6,
        )
        with self.voiceover(
            text="""These bottom-row operations are... deeply strange.
                    They're the kinds of houses you'd skip entirely.
                    But mathematically? 
                    They're just as valid as the classics."""
        ):
            self.wait()

        self.wait(0.5)

        with self.voiceover(
            text="""So the next time a child asks [kid sing-songy] "trick or treat?", 
                    you now have the mathematically correct response: 
                    [annoying high-pitched nasal pedantic] "That depends—which logical operator are you implementing?"
                    [quick laugh] ...though I wouldn't recommend it if you don't want your house getting egged."""
        ):
            self.wait()
        self.play(FadeOut(gallery), run_time=1.2)
        self.wait(0.5)

    def create_panel(self, op_name, scale_factor=1.0):
        panel_bg = RoundedRectangle(width=5.5, height=4, corner_radius=0.2)

        title = Text(f"Trick {op_name} Treat").scale(0.7)
        title.move_to(panel_bg.get_top() + DOWN * 0.3)

        c1 = Circle(radius=1.1, color=BLACK).move_to(LEFT * 0.6)
        c2 = Circle(radius=1.1, color=BLACK).move_to(RIGHT * 0.6)
        venn_diagram = VGroup(c1, c2)

        face_elements = VGroup()
        filled_shape = VGroup()

        if op_name == "OR":
            panel_bg.set_fill(GREY, opacity=1)
            shape = Union(c1, c2).set_fill(ORANGE, opacity=1)
            filled_shape.add(shape)
            face_elements.add(self.create_face(shape))
        elif op_name == "AND":
            panel_bg.set_fill(GREY, opacity=1)
            shape = Intersection(c1, c2).set_fill(ORANGE, opacity=1)
            filled_shape.add(shape)
            face_elements.add(self.create_face(shape, scale=0.6))
        elif op_name == "XOR":
            panel_bg.set_fill(GREY, opacity=1)
            shape = Exclusion(c1, c2).set_fill(ORANGE, opacity=1)
            filled_shape.add(shape)
            left_part = Difference(c1, c2)
            right_part = Difference(c2, c1)
            face_elements.add(
                self.create_face(left_part, "left"),
                self.create_face(right_part, "right"),
            )
        elif op_name == "NOR":
            panel_bg.set_fill(ORANGE, opacity=1)
            shape = Union(c1, c2).set_fill(GREY, opacity=1)
            filled_shape.add(shape)
            face_elements.add(
                self.create_eye().move_to(LEFT * 1.5 + UP * 0.8),
                self.create_eye().move_to(RIGHT * 1.5 + UP * 0.8),
                self.create_mouth_part().move_to(LEFT * 1.5 + DOWN * 0.5),
                self.create_mouth_part().move_to(RIGHT * 1.5 + DOWN * 0.5),
            )
        elif op_name == "NAND":
            panel_bg.set_fill(ORANGE, opacity=1)
            shape = Intersection(c1, c2).set_fill(GREY, opacity=1)
            c1_filled = c1.copy().set_fill(ORANGE, opacity=1)
            c2_filled = c2.copy().set_fill(ORANGE, opacity=1)
            filled_shape.add(c1_filled, c2_filled, shape)
            left_part = Difference(c1, c2)
            right_part = Difference(c2, c1)
            face_elements.add(
                self.create_face(left_part, "left"),
                self.create_face(right_part, "right"),
            )
        elif op_name == "XNOR":
            panel_bg.set_fill(ORANGE, opacity=1)

            left_diff = Difference(c1, c2).set_fill(GREY, opacity=1)
            right_diff = Difference(c2, c1).set_fill(GREY, opacity=1)
            intersection = Intersection(c1, c2).set_fill(ORANGE, opacity=1)

            filled_shape.add(left_diff, right_diff, intersection)

            intersection_for_pos = Intersection(c1, c2)
            face_elements.add(
                self.create_eye().move_to(panel_bg.get_corner(UL) + DR * 0.5),
                self.create_eye().move_to(panel_bg.get_corner(UR) + DL * 0.5),
                self.create_mouth_part()
                .scale(0.5)
                .move_to(intersection_for_pos.get_center()),
            )

        base = VGroup(panel_bg, filled_shape, venn_diagram, title)
        panel = VGroup(base, face_elements)
        if scale_factor != 1.0:
            panel.scale(scale_factor)
        return panel

    def create_setup_panel(self):
        panel_bg = RoundedRectangle(width=5.5, height=4, corner_radius=0.2).set_fill(
            GREY, opacity=1
        )
        title = Text("Trick or Treat?").scale(0.7)
        title.move_to(panel_bg.get_top() + DOWN * 0.3)

        c1 = Circle(radius=1.1, color=BLACK, stroke_width=6).move_to(LEFT * 0.6)
        c2 = Circle(radius=1.1, color=BLACK, stroke_width=6).move_to(RIGHT * 0.6)
        venn = VGroup(c1, c2)

        label_a = Text("A", font_size=32).next_to(c1, DOWN, buff=0.25)
        label_b = Text("B", font_size=32).next_to(c2, DOWN, buff=0.25)

        return VGroup(panel_bg, venn, title, label_a, label_b)

    def create_legend(self):
        treat_swatch = (
            Square(side_length=0.35)
            .set_fill(ORANGE, opacity=1)
            .set_stroke(BLACK, width=2)
        )
        treat_label = Text("Treat", font_size=28).next_to(treat_swatch, RIGHT, buff=0.2)
        treat = VGroup(treat_swatch, treat_label)

        trick_swatch = (
            Square(side_length=0.35)
            .set_fill(GREY, opacity=1)
            .set_stroke(BLACK, width=2)
        )
        trick_label = Text("Trick", font_size=28).next_to(trick_swatch, RIGHT, buff=0.2)
        trick = VGroup(trick_swatch, trick_label)

        legend = VGroup(treat, trick).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_edge(RIGHT, buff=0.5)
        return legend

    def transition_panel(self, current_panel, next_panel):
        next_panel.move_to(current_panel.get_center())
        self.play(ReplacementTransform(current_panel, next_panel), run_time=0.9)
        return next_panel

    def create_gallery(self):
        operations = ["OR", "AND", "XOR", "NOR", "NAND", "XNOR"]
        panels = [self.create_panel(op) for op in operations]
        grid = VGroup(*panels).arrange_in_grid(rows=2, cols=3, buff=0.55)
        grid.scale(0.78)
        return grid

    def create_caption(self, lines):
        caption_lines = [Text(line, font_size=32) for line in lines]
        caption = VGroup(*caption_lines).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        caption.to_edge(DOWN, buff=0.6)
        caption.set_x(0)
        return caption

    def create_eye(self):
        return Circle(radius=0.15, color=BLACK, fill_opacity=1)

    def create_mouth_part(self):
        mouth = ParametricFunction(
            lambda t: [t, 0.15 * np.sin(t * PI * 5), 0], t_range=[-0.4, 0.4]
        )
        mouth.set_stroke(color=BLACK, width=8)
        return mouth

    def create_face(self, target_shape, side="full", scale=1.0):
        face = VGroup()
        if side in ("full", "left"):
            eye1_pos = target_shape.get_center() + UL * 0.4 * scale
            face.add(self.create_eye().scale(scale).move_to(eye1_pos))
        if side in ("full", "right"):
            eye2_pos = target_shape.get_center() + UR * 0.4 * scale
            face.add(self.create_eye().scale(scale).move_to(eye2_pos))

        if side == "full":
            mouth = self.create_mouth_part()
            mouth_pos = target_shape.get_center() + DOWN * 0.2 * scale
            face.add(mouth.scale(scale).move_to(mouth_pos))
        elif side == "left":
            mouth = self.create_mouth_part().rotate(-PI / 12)
            mouth_pos = target_shape.get_center() + DOWN * 0.2 * scale + RIGHT * 0.1
            face.add(mouth.scale(scale).move_to(mouth_pos))
        elif side == "right":
            mouth = self.create_mouth_part().rotate(PI / 12)
            mouth_pos = target_shape.get_center() + DOWN * 0.2 * scale + LEFT * 0.1
            face.add(mouth.scale(scale).move_to(mouth_pos))

        return face
