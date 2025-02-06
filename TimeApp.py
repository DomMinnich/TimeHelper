# Dominic Minnich 2025

import tkinter as tk
from tkinter import ttk

class TimeHelperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="#2B2B2B")

        self.withdraw()
        self.alpha_value = 0.0
        self.attributes("-alpha", self.alpha_value)

        self.title("Time Helper -Developed by Dominic Minnich")
        self.geometry("600x550")

        self.create_custom_style()

        target_frame = ttk.LabelFrame(
            self, text="Weekly Target Hours", style="ThinLine.TLabelframe"
        )
        target_frame.pack(padx=10, pady=10, fill="x")
        ttk.Label(
            target_frame, text="Total hours to work this week:", style="ThinLine.TLabel"
        ).pack(side="left", padx=5, pady=5)

        self.weekly_target = tk.DoubleVar(value=20)
        ttk.Entry(
            target_frame,
            textvariable=self.weekly_target,
            width=10,
            style="ThinLine.TEntry",
        ).pack(side="left", padx=5, pady=5)

        worked_frame = ttk.LabelFrame(
            self, text="Hours Already Worked", style="ThinLine.TLabelframe"
        )
        worked_frame.pack(padx=10, pady=10, fill="x")
        self.worked_vars = {}
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        for day in days:
            day_frame = ttk.Frame(worked_frame, style="ThinLine.TFrame")
            day_frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(
                day_frame, text=f"{day}:", width=12, style="ThinLine.TLabel"
            ).pack(side="left")
            var = tk.DoubleVar(value=0)
            self.worked_vars[day] = var
            ttk.Entry(
                day_frame, textvariable=var, width=10, style="ThinLine.TEntry"
            ).pack(side="left", padx=5)

        style_button = ttk.Button(
            self,
            text="Calculate Remaining Hours",
            command=self.calculate_remaining,
            style="Accent.TButton",
        )
        style_button.pack(pady=10)

        style_button.bind(
            "<Enter>", lambda e: style_button.configure(style="AccentHover.TButton")
        )
        style_button.bind(
            "<Leave>", lambda e: style_button.configure(style="Accent.TButton")
        )

        self.result_label = ttk.Label(
            self, text="Remaining Hours:", style="ThinLineBig.TLabel"
        )
        self.result_label.pack(pady=5)

        slider_frame = ttk.LabelFrame(
            self, text="Work Period Double Slider", style="ThinLine.TLabelframe"
        )
        slider_frame.pack(padx=10, pady=10, fill="x")

        # Start Time Slider (default 8 AM)
        start_frame = ttk.Frame(slider_frame, style="ThinLine.TFrame")
        start_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(
            start_frame, text="Start Time (hours): ", style="ThinLine.TLabel"
        ).pack(side="left")

        self.start_time = tk.DoubleVar(value=8)
        self.start_slider = ttk.Scale(
            start_frame,
            from_=0,
            to=24,
            variable=self.start_time,
            command=self.update_slider_label,
            orient="horizontal",
            length=300,
            style="ThinLineHorizontal.TScale",
        )
        self.start_slider.pack(side="left", padx=5)

        self.start_time_label = ttk.Label(
            start_frame,
            text=self.format_time(self.start_time.get()),
            style="ThinLine.TLabel",
        )
        self.start_time_label.pack(side="left", padx=5)

        end_frame = ttk.Frame(slider_frame, style="ThinLine.TFrame")
        end_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(end_frame, text="End Time (hours): ", style="ThinLine.TLabel").pack(
            side="left"
        )

        self.end_time = tk.DoubleVar(value=17)
        self.end_slider = ttk.Scale(
            end_frame,
            from_=0,
            to=24,
            variable=self.end_time,
            command=self.update_slider_label,
            orient="horizontal",
            length=300,
            style="ThinLineHorizontal.TScale",
        )
        self.end_slider.pack(side="left", padx=5)

        self.end_time_label = ttk.Label(
            end_frame,
            text=self.format_time(self.end_time.get()),
            style="ThinLine.TLabel",
        )
        self.end_time_label.pack(side="left", padx=5)

        self.slider_result_label = ttk.Label(
            slider_frame, text="Work Period Duration:", style="ThinLineBig.TLabel"
        )
        self.slider_result_label.pack(pady=5)

        self.update_slider_label()

        self.deiconify()
        self.fade_in()

    def fade_in(self):
        """
        Simple fade-in animation by incrementing the alpha value of the window.
        """
        self.alpha_value += 0.05
        if self.alpha_value > 1:
            self.alpha_value = 1
        self.attributes("-alpha", self.alpha_value)
        if self.alpha_value < 1:
            self.after(20, self.fade_in)

    def create_custom_style(self):
        """
        Create a custom ttk style (theme) using a soft-black background and soft-green highlights.
        We will define custom styles for frames, labels, entries, and buttons.

        Importantly, we define a layout for 'Horizontal.ThinLineHorizontal.TScale'
        by cloning the built-in 'Horizontal.TScale' layout.
        """
        style = ttk.Style(self)

        style.theme_create(
            "SoftGreenBlack",
            parent="clam",
            settings={
                "TFrame": {"configure": {"background": "#2B2B2B", "borderwidth": 0}},
                "TLabelframe": {
                    "configure": {
                        "background": "#2B2B2B",
                        "borderwidth": 1,
                        "relief": "groove",
                    }
                },
                "TLabelframe.Label": {
                    "configure": {
                        "background": "#2B2B2B",
                        "foreground": "#7EC07E",
                        "padding": 4,
                    }
                },
                "TLabel": {
                    "configure": {"background": "#2B2B2B", "foreground": "#7EC07E"}
                },
                "TEntry": {
                    "configure": {
                        "fieldbackground": "#3C3C3C",
                        "foreground": "#FFFFFF",
                        "insertcolor": "#FFFFFF",
                    }
                },
                "TButton": {
                    "configure": {
                        "background": "#2B2B2B",
                        "foreground": "#FFFFFF",
                        "padding": (6, 2),
                        "relief": "flat",
                    },
                    "map": {
                        "foreground": [("active", "#2B2B2B"), ("disabled", "#7A7A7A")],
                        "background": [("active", "#7EC07E"), ("disabled", "#4E4E4E")],
                    },
                },
                "Horizontal.TScale": {
                    "configure": {
                        "background": "#2B2B2B",
                        "troughcolor": "#3C3C3C",
                        "relief": "flat",
                        "bordercolor": "#3C3C3C",
                        "lightcolor": "#7EC07E",
                        "darkcolor": "#2B2B2B",
                    }
                },
            },
        )

        style.theme_use("SoftGreenBlack")

        style.configure("ThinLine.TFrame", background="#2B2B2B")
        style.configure(
            "ThinLine.TLabelframe",
            background="#2B2B2B",
            foreground="#7EC07E",
            borderwidth=1,
            relief="solid",
        )
        style.configure("ThinLine.TLabel", background="#2B2B2B", foreground="#7EC07E")
        style.configure(
            "ThinLineBig.TLabel",
            background="#2B2B2B",
            foreground="#7EC07E",
            font=("Arial", 12, "bold"),
        )
        style.configure(
            "ThinLine.TEntry",
            fieldbackground="#3C3C3C",
            foreground="#FFFFFF",
            insertcolor="#FFFFFF",
            borderwidth=1,
            relief="solid",
        )

        style.configure(
            "Accent.TButton",
            background="#2B2B2B",
            foreground="#FFFFFF",
            padding=(8, 4),
            font=("Arial", 10, "bold"),
            borderwidth=1,
            relief="solid",
        )
        style.map(
            "Accent.TButton",
            foreground=[("active", "#2B2B2B")],
            background=[("active", "#7EC07E")],
        )

        style.configure(
            "AccentHover.TButton",
            background="#5EA05E",
            foreground="#2B2B2B",
            padding=(8, 4),
            font=("Arial", 10, "bold"),
            borderwidth=1,
            relief="solid",
        )

        style.layout(
            "Horizontal.ThinLineHorizontal.TScale", style.layout("Horizontal.TScale")
        )

        style.configure(
            "Horizontal.ThinLineHorizontal.TScale",
            background="#2B2B2B",
            troughcolor="#3C3C3C",
            bordercolor="#2B2B2B",
            lightcolor="#7EC07E",
            darkcolor="#2B2B2B",
            sliderlength=14,
        )

    def format_time(self, time_val):
        """
        Convert float hours to 12-hour HH:MM format with AM/PM.
        """
        hour_24 = int(time_val) % 24
        minute = int(round((time_val - int(time_val)) * 60))
        if minute == 60:
            hour_24 = (hour_24 + 1) % 24
            minute = 0
        period = "AM" if hour_24 < 12 else "PM"
        hour_12 = hour_24 % 12
        if hour_12 == 0:
            hour_12 = 12
        return f"{hour_12:02d}:{minute:02d} {period}"

    def format_duration(self, duration_val):
        """
        Format duration (in hours) as H hours M minutes (without AM/PM).
        """
        hours = int(duration_val)
        minutes = int(round((duration_val - hours) * 60))
        if minutes == 60:
            hours += 1
            minutes = 0
        return f"{hours}h {minutes}m"

    def calculate_remaining(self):
        """
        Calculate how many hours remain based on the target minus what's already worked.
        Then auto-adjust the end slider to reflect that block of time following the start time.
        """
        total_worked = sum(var.get() for var in self.worked_vars.values())
        remaining = self.weekly_target.get() - total_worked
        self.result_label.config(text=f"Remaining Hours: {remaining:.2f}")

        new_end = self.start_time.get() + remaining
        if new_end > 24:
            new_end = 24
        self.end_time.set(new_end)
        self.update_slider_label()

    def update_slider_label(self, event=None):
        """
        Update the display label for start/end times and compute the work duration.
        """
        start = self.start_time.get()
        end = self.end_time.get()
        self.start_time_label.config(text=self.format_time(start))
        self.end_time_label.config(text=self.format_time(end))

        duration = max(0, end - start)
        self.slider_result_label.config(
            text=f"Work Period Duration: {self.format_duration(duration)} "
            f"(from {self.format_time(start)} to {self.format_time(end)})"
        )


if __name__ == "__main__":
    app = TimeHelperApp()
    app.mainloop()
