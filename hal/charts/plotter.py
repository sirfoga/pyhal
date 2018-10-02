# !/usr/bin/python3
# coding: utf-8


""" Show elegant plots in any dimension """

import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider
from scipy import linspace


class Plot2d(object):
    """ 2d plot """

    @staticmethod
    def scatter(vector_x, vector_y):
        """
        :param vector_x: vector in x axis
        :param vector_y: vector in y axis
        :return: 2d scatter plot
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
        :param function_x: function in x value
        :param function_y: function in y value
        :param min_val: minimum value
        :param max_val: maximum value
        :param points: number of points to display
        :return: 2d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                Plot2d.param(function_x, function_y, max_val, min_val, points)

    @staticmethod
    def plot(function, min_val, max_val, points):
        """
        :param function: function to plot
        :param min_val: minimum value
        :param max_val: maximum value
        :param points: number of points
        :return: plot 2d function
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                Plot2d.plot(function, max_val, min_val, points)
            else:
                x_values = linspace(min_val, max_val, points)
                plt.plot(x_values, function(x_values))
                plt.show()


class Plot3d(object):
    """ 3D plot """

    @staticmethod
    def scatter(vector_x, vector_y, vector_z):
        """
        :param vector_x: vector in x axis
        :param vector_y: vector in y axis
        :param vector_z: vector in z axis
        :return: plot 3d scattered points
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
        :param function_x: function in x
        :param function_y: function in y
        :param function_z: function in z
        :param min_val: minimum
        :param max_val: maximum
        :param points: number of points
        :return: 3d parametric graph of given function from min to max
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
    def plot(function, min_x, max_x, points_x, min_y, max_y, points_y):
        """
        :param function: function to plot
        :param min_x: minimum of x-values
        :param max_x: maximum of x-values
        :param points_x: points in x axis
        :param min_y: minimum of y-values
        :param max_y: maximum of y-values
        :param points_y: points in y axis
        :return: plot 3d function
        """
        if points_x < 0 or points_y < 0:
            raise ValueError("Number of points to plot must be positive.")

        if min_x > max_x:
            Plot3d.plot(function, max_x, min_x, points_x, min_y, max_y,
                        points_y)

        if min_y > max_y:
            Plot3d.plot(function, min_x, max_x, points_x, max_y, min_y,
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
        z_axis = function(x_axis, y_axis)

        # plot
        chart.plot_surface(
            x_axis, y_axis, z_axis,
            cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0
        )
        plt.show()


class Plot4d(object):
    """ 4D plot generator with slider """

    @staticmethod
    def scatter(vector_x, vector_y, vector_z, vector_w):
        """
        :param vector_x: vector in x axis
        :param vector_y: vector in y axis
        :param vector_z: vector in z axis
        :param vector_w: vector in w axis
        :return: plot 4d scattered points
        """
        if len(vector_x) == len(vector_y) == len(vector_z) == len(vector_w):
            pass
        else:
            raise ValueError("Cannot plot vectors of different length.")

    @staticmethod
    def plot(function, min_x, max_x, min_y, max_y, min_z, max_z,
             precision=0.5, kind="contour"):
        """
        :param function: function to plot
        :param min_x: minimum of x-values
        :param max_x: maximum of x-values
        :param min_y: minimum of y-values
        :param max_y: maximum of y-values
        :param min_z: minimum of z-values
        :param max_z: maximum of z-values
        :param precision: precision
        :param kind: slice: x cont -> 3d plot with y, z variables in plane
            and w as "z"-axis contour: x cont -> 3d plot with y,z variables in
            plane and w colored
        :return: plot 4d function
        """

        if precision < 0:
            raise ValueError("Precision cannot be negative.")

        if min_x > max_x:
            Plot4d.plot(function, max_x, min_x, min_y, max_y, min_z, max_z,
                        precision, kind)

        if min_y > max_y:
            Plot4d.plot(function, min_x, max_x, max_y, min_y, min_z, max_z,
                        precision, kind)

        if min_z > max_z:
            Plot4d.plot(function, min_x, max_x, min_y, max_y, max_z, min_z,
                        precision, kind)

        if kind != "slice" and kind != "contour":
            raise ValueError(
                "Plot type not supported, only \"slice\" and \"contour\" are.")

        def set_labels(graph, label_x, label_y, label_z):
            """
            :param graph: plot
            :param label_x: new label on x axis
            :param label_y: new label on y axis
            :param label_z: new label on z axis
            :return: set given labels to axes of graph
            """

            graph.set_xlabel(label_x)
            graph.set_ylabel(label_y)
            graph.set_zlabel(label_z)

        def set_limits(graph):
            """
            :param graph: plot
            :return: set given limits to axes of graph
            """

            graph.set_xlim(min_x, max_x)
            graph.set_ylim(min_y, max_y)
            graph.set_zlim(min_z, max_z)

        def get_precision(min_val, max_val):
            """
            :param min_val: minimum
            :param max_val: maximum
            :return: default number of points = interval / 0.1
            """

            return int((max_val - min_val) * (1 + precision))

        def get_precision_delta(min_val, max_val):
            """
            :param min_val: minimum
            :param max_val: maximum
            :return: default Delta = interval / points
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
                :return: re-plot
                """

                chart.clear()
                x_const = slider.val
                z_axis = function(x_const, x_axis, y_axis)
                chart.plot_surface(
                    x_axis, y_axis, z_axis, alpha=0.3, linewidth=2.0
                )
                set_labels(chart, "y", "z", "w")

            slider.on_changed(update)
            set_labels(chart, "y", "z", "w")
            # plot
            plt.show()
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
                :return: re-plot plot
                """

                chart.clear()  # re-plot
                x_const = slider.val
                z_axis = []

                # add new points
                for i, _ in enumerate(x_axis):
                    z_axis.append(function(x_const, x_axis[i], y_axis[i]))

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
