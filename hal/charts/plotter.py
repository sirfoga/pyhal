# -*- coding: utf-8 -*-

""" Show elegant plots in any dimension """

import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider
from scipy import linspace


class Plot2d:
    """2d plot"""

    @staticmethod
    def scatter(vector_x, vector_y):
        """
        Plots scatter data

        # Arguments
            vector_x: vector in x axis
            vector_y: vector in y axis

        # Returns
            Shows 2d scatter plot
        """
        if len(vector_x) == len(vector_y):
            # fig = plt.figure()
            # ax = fig.add_subplot(111)
            # ax.scatter(vector_x, vector_y, c="r", marker="o")

            plt.plot(vector_x, vector_y, "-o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    @staticmethod
    def param(function_x, function_y, min_val, max_val, points):
        """
        Plots parametric data

        # Arguments
            function_x: function in x value
            function_y: function in y value
            min_val: minimum value
            max_val: maximum value
            points: number of points to display

        # Returns
            Shows 2d parametric graph of given function from min to max
        """
        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                Plot2d.param(function_x, function_y, max_val, min_val, points)

    @staticmethod
    def plot(func, min_val, max_val, points):
        """
        Plots data

        # Arguments
            func: function to plot
            min_val: minimum value
            max_val: maximum value
            points: number of points

        # Returns
            Plots 2d function
        """
        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                Plot2d.plot(func, max_val, min_val, points)
            else:
                x_values = linspace(min_val, max_val, points)
                plt.plot(x_values, func(x_values))
                plt.show()


class Plot3d:
    """3D plot"""

    @staticmethod
    def scatter(vector_x, vector_y, vector_z):
        """
        Plots scatter data

        # Arguments
            vector_x: vector in x axis
            vector_y: vector in y axis
            vector_z: vector in z axis

        # Returns
            Plots 3d scattered points
        """
        if len(vector_x) == len(vector_y) == len(vector_z):
            # general settings
            fig = plt.figure()
            chart = fig.add_subplot(111, projection='3d')

            # plot
            chart.scatter(vector_x, vector_y, vector_z, c="r", marker="o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    @staticmethod
    def param(function_x, function_y, function_z, min_val, max_val,
              points):
        """
        Plots parametric functions

        # Arguments
            function_x: function in x
            function_y: function in y
            function_z: function in z
            min_val: minimum
            max_val: maximum
            points: number of points

        # Returns
            Shows 3d parametric graph of given function from min to max
        """
        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                Plot3d.param(
                    function_x,
                    function_y,
                    function_z,
                    max_val,
                    min_val,
                    points
                )
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
            plt.show()

    @staticmethod
    def plot(func, min_x, max_x, points_x, min_y, max_y, points_y):
        """
        Plots function

        # Arguments
            func: function to plot
            min_x: minimum of x-values
            max_x: maximum of x-values
            points_x: points in x axis
            min_y: minimum of y-values
            max_y: maximum of y-values
            points_y: points in y axis

        # Returns
            Plots 3d function
        """
        if points_x < 0 or points_y < 0:
            raise ValueError("Number of points to plot must be positive.")

        if min_x > max_x:
            Plot3d.plot(func, max_x, min_x, points_x, min_y, max_y,
                        points_y)

        if min_y > max_y:
            Plot3d.plot(func, min_x, max_x, points_x, max_y, min_y,
                        points_y)

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
        plt.show()


class Plot4d:
    """4D plot generator with slider"""

    @staticmethod
    def scatter(vector_x, vector_y, vector_z, vector_w):
        """
        Plots scatter data

        # Arguments
            vector_x: vector in x axis
            vector_y: vector in y axis
            vector_z: vector in z axis
            vector_w: vector in w axis

        # Returns
            Plots 4d scattered points
        """
        if len(vector_x) == len(vector_y) == len(vector_z) == len(vector_w):
            pass
        else:
            raise ValueError("Cannot plot vectors of different length.")

    @staticmethod
    def plot(func, min_x, max_x, min_y, max_y, min_z, max_z,
             precision=0.5, kind="contour"):
        """
        Plots function

        # Arguments
            func: function to plot
            min_x: minimum of x-values
            max_x: maximum of x-values
            min_y: minimum of y-values
            max_y: maximum of y-values
            min_z: minimum of z-values
            max_z: maximum of z-values
            precision: precision (Default value = 0.5)
            kind: x cont -> 3d plot with y, z variables in plane
                and w as "z"-axis contour: x cont -> 3d plot with y,z variables
                in plane and w colored (Default value = "contour")

        # Returns
            Plots 4d function
        """
        if precision < 0:
            raise ValueError("Precision cannot be negative.")

        if min_x > max_x:
            Plot4d.plot(func, max_x, min_x, min_y, max_y, min_z, max_z,
                        precision, kind)

        if min_y > max_y:
            Plot4d.plot(func, min_x, max_x, max_y, min_y, min_z, max_z,
                        precision, kind)

        if min_z > max_z:
            Plot4d.plot(func, min_x, max_x, min_y, max_y, max_z, min_z,
                        precision, kind)

        if kind != "slice" and kind != "contour":
            raise ValueError(
                "Plot type not supported, only \"slice\" and \"contour\" are.")

        def set_labels(graph, label_x, label_y, label_z):
            """
            Set chart labels

            # Arguments
                graph: plot
               label_x: new label on x axis
                label_y: new label on y axis
                label_z: new label on z axis

            # Returns
                Sets given labels to axes of graph
            """
            graph.set_xlabel(label_x)
            graph.set_ylabel(label_y)
            graph.set_zlabel(label_z)

        def set_limits(graph):
            """
            Set chart limits

            # Arguments
                graph: plot

            # Returns
                Sets given limits to axes of graph
            """
            graph.set_xlim(min_x, max_x)
            graph.set_ylim(min_y, max_y)
            graph.set_zlim(min_z, max_z)

        def get_precision(min_val, max_val):
            """
            Calculates precision

            # Arguments
                min_val: minimum
                max_val: maximum

            # Returns
                precision: prevision of values
            """
            return int((max_val - min_val) * (1 + precision))

        def get_precision_delta(min_val, max_val):
            """
            Calculates precision delta

            # Arguments
                min_val: minimum
                max_val: maximum

            # Returns
                delta: Precision delta
            """
            return float(max_val - min_val) / float(10 * precision)

        if kind == "slice":
            chart = plt.axes(projection="3d")  # general settings
            points_x = get_precision(min_x, max_x)
            points_y = get_precision(min_y, max_z)

            x_axis = numpy.outer(linspace(min_x, max_x, points_x), points_x)
            y_axis = numpy.outer(
                linspace(min_y, max_y, points_y).flatten(), points_y
            ).T
            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", min_x, max_x, valinit=min_x)

            def update(val):
                """
                Updates chart with value

                # Arguments
                    val: value

                # Returns
                    Re-plots
                """
                chart.clear()
                x_const = slider.val
                z_axis = func(x_const, x_axis, y_axis)
                chart.plot_surface(
                    x_axis, y_axis, z_axis, alpha=0.3, linewidth=2.0
                )
                set_labels(chart, "y", "z", "w")

            slider.on_changed(update)
            set_labels(chart, "y", "z", "w")
            plt.show()  # plot
        else:  # kind = contour
            # general settings
            fig = plt.figure()
            chart = fig.gca(projection="3d")

            # create axes
            x_axis = numpy.arange(min_x, max_x, get_precision_delta(
                min_x, max_x)).tolist()
            y_axis = numpy.arange(min_y, max_y, get_precision_delta(
                min_y, max_y)).tolist()
            x_axis, y_axis = numpy.meshgrid(x_axis, y_axis)

            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", min_x, max_x, valinit=min_x)

            # update

            def update(val):
                """
                Updates chart with value

                # Arguments
                    val: value

                # Returns
                    Re-plots
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

            slider.on_changed(update)
            set_limits(chart)
            plt.show()
