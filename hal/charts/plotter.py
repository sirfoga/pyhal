# -*- coding: utf-8 -*-

"""Show elegant plots in any dimension """

import abc

import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider
from scipy import linspace


class Plotter:
    """Plots something in N-dimensional space"""

    @abc.abstractmethod
    def scatter(self, vectors):
        """Plots scatter data

        :param vectors: list of vectors (x, y, ...)
        """
        pass

    @abc.abstractmethod
    def param(self, functions, min_val, max_val, points):
        """Plots parametric data

        :param functions: functions to plot (x, y ...)
        :param min_val: minimum value
        :param max_val: maximum value
        :param points: number of points to display
        """

        pass

    @abc.abstractmethod
    def plot(self, func, mins, maxs, points):
        """Plots function

        :param func: function to plot
        :param mins: minimum of values (x, y ...)
        :param maxs: maximum of values (x, y ...)
        :param points: points in axis (x, y ...)
        """
        pass

    @staticmethod
    def show_plot():
        """Shows plot"""
        plt.legend()
        plt.show()


class Plot2d(Plotter):
    """2d plot"""

    def scatter(self, vectors):
        """

        :param vectors:
        """
        vector_x = vectors[0]
        vector_y = vectors[1]
        plt.plot(vector_x, vector_y, "-o")
        self.show_plot()

    def param(self, functions, min_val, max_val, points):
        """

        :param functions:
        :param min_val:
        :param max_val:
        :param points:
        """
        function_x = functions[0]
        function_y = functions[1]

        # limits and plot
        theta = linspace(min_val, max_val, points)
        x_axis = function_x(theta)
        y_axis = function_y(theta)
        plt.plot(x_axis, y_axis)

        self.show_plot()

    def plot(self, func, mins, maxs, points):
        """

        :param func: 
        :param mins: 
        :param maxs: 
        :param points: 
        """
        min_x = mins[0]
        max_x = maxs[0]
        points = points[0]
        x_values = linspace(min_x, max_x, points)
        plt.plot(x_values, func(x_values))
        self.show_plot()


class Plot3d(Plotter):
    """3D plot"""

    def scatter(self, vectors):
        """

        :param vectors: 
        """
        vector_x = vectors[0]
        vector_y = vectors[1]
        vector_z = vectors[2]

        # general settings
        fig = plt.figure()
        chart = fig.add_subplot(111, projection='3d')

        # plot
        chart.scatter(vector_x, vector_y, vector_z, c="r", marker="o")
        self.show_plot()

    def param(self, functions, min_val, max_val, points):
        """

        :param functions: 
        :param min_val: 
        :param max_val: 
        :param points: 
        """
        function_x = functions[0]
        function_y = functions[1]
        function_z = functions[2]

        # general settings
        fig = plt.figure()
        chart = fig.gca(projection="3d")

        # limits and plot
        theta = linspace(min_val, max_val, points)
        x_axis = function_x(theta)
        y_axis = function_y(theta)
        z_axis = function_z(theta)
        chart.plot(x_axis, y_axis, z_axis)
        chart.legend()

        # show
        self.show_plot()

    def plot(self, func, mins, maxs, points):
        """

        :param func: 
        :param mins: 
        :param maxs: 
        :param points: 
        """
        min_x, min_y = mins[0], mins[1]
        max_x, max_y = maxs[0], maxs[1]
        points_x, points_y = points[0], points[1]

        # general settings
        chart = plt.axes(projection="3d")

        # points
        x_axis = numpy.outer(
            linspace(min_x, max_x, points_x), numpy.ones(points_x)
        )
        y_axis = numpy.outer(
            linspace(min_y, max_y, points_y), numpy.ones(points_y)
        ).T
        z_axis = func(x_axis, y_axis)

        # plot
        chart.plot_surface(
            x_axis, y_axis, z_axis,
            cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0
        )
        self.show_plot()


class Plot4d(Plotter):
    """4D plot generator with slider"""

    def scatter(self, vectors):
        """

        :param vectors: 
        """
        raise ValueError("Cannot plot 4D vectors in 2D space")

    def param(self, functions, min_val, max_val, points):
        """

        :param functions: 
        :param min_val: 
        :param max_val: 
        :param points: 
        """
        raise ValueError("Cannot plot 4D function in 2D space")

    def plot(self, func, mins, maxs, points, precision=0.5, kind="slice"):
        """

        :param func: 
        :param mins: 
        :param maxs: 
        :param points: 
        :param precision:  (Default value = 0.5)
        :param kind:  (Default value = "slice")
        """
        min_x, min_y, min_z = mins[0], mins[1], mins[2]
        max_x, max_y, max_z = maxs[0], maxs[1], maxs[2]

        def set_labels(graph, label_x, label_y, label_z):
            """Sets given labels to axes of graph

            :param graph: plot
            :param label_x: new label on x axis
            :param label_y: new label on y axis
            :param label_z: new label on z axis
            """
            graph.set_xlabel(label_x)
            graph.set_ylabel(label_y)
            graph.set_zlabel(label_z)

        def set_limits(graph):
            """Set chart limits to axes of graph

            :param graph: plot
            """
            graph.set_xlim(min_x, max_x)
            graph.set_ylim(min_y, max_y)
            graph.set_zlim(min_z, max_z)

        def get_precision(min_val, max_val):
            """Calculates precision

            :param min_val: minimum
            :param max_val: maximum
            :returns: precision: prevision of values
            """
            return int((max_val - min_val) * (1 + precision))

        def get_precision_delta(min_val, max_val):
            """Calculates precision delta

            :param min_val: minimum
            :param max_val: maximum
            :returns: delta: Precision delta
            """
            return float(max_val - min_val) / float(10 * precision)

        def plot_slice():
            """ """
            chart = plt.axes(projection="3d")  # general settings
            points_x = get_precision(min_x, max_x)
            points_y = get_precision(min_y, max_z)

            x_axis = numpy.outer(linspace(min_x, max_x, points_x), points_x)
            y_axis = numpy.outer(
                linspace(min_y, max_y, points_y).flatten(), points_y
            ).T

            def update(val):
                """Updates chart with value

                :param val: value
                """
                chart.clear()
                x_const = slider.val
                z_axis = func(x_const, x_axis, y_axis)
                chart.plot_surface(
                    x_axis, y_axis, z_axis, alpha=0.3, linewidth=2.0
                )
                set_labels(chart, "y", "z", "w")

            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", min_x, max_x, valinit=min_x)

            slider.on_changed(update)
            set_limits(chart)
            self.show_plot()

            slider.on_changed(update)
            set_labels(chart, "y", "z", "w")

        def plot_countour():
            """Plots countour
            """
            # general settings
            fig = plt.figure()
            chart = fig.gca(projection="3d")

            # create axes
            x_axis = numpy.arange(min_x, max_x, get_precision_delta(
                min_x, max_x)).tolist()
            y_axis = numpy.arange(min_y, max_y, get_precision_delta(
                min_y, max_y)).tolist()
            x_axis, y_axis = numpy.meshgrid(x_axis, y_axis)

            def update(val):
                """Updates chart with value

                :param val: value
                """
                chart.clear()  # re-plot
                x_const = slider.val
                z_axis = []

                # add new points
                for i, _ in enumerate(x_axis):
                    z_axis.append(func(x_const, x_axis[i], y_axis[i]))

                # show
                chart.contour(
                    x_axis, y_axis, z_axis, zdir="x", offset=min_x
                )
                chart.contour(
                    x_axis, y_axis, z_axis, zdir="y", offset=min_y
                )
                chart.contour(
                    x_axis, y_axis, z_axis, zdir="z", offset=min_z
                )
                chart.contour(x_axis, y_axis, z_axis, extend3d=True)
                set_labels(chart, "y", "z", "w")

            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", min_x, max_x, valinit=min_x)

            slider.on_changed(update)
            set_limits(chart)

        if kind == "slice":
            plot_slice()
        elif kind == "countour":
            plot_countour()

        self.show_plot()
