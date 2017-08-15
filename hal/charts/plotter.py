# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Show elegant plots in any dimension. """

import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider
from scipy import linspace


class Plot2d(object):
    """ 2d plot """

    @staticmethod
    def scatter(vectorx, vectory):
        """
        :param vectorx: vector in x axis
        :param vectory: vector in y axis
        :return: 2d scatter plot
        """

        if len(vectorx) == len(vectory):
            # fig = plt.figure()
            # ax = fig.add_subplot(111)
            # ax.scatter(vectorx, vectory, c="r", marker="o")

            plt.plot(vectorx, vectory, "-o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    def param(self, functionx, functiony, min_val, max_val, points):
        """
        :param functionx: function in x value
        :param functiony: function in y value
        :param min_val: minimum value
        :param max_val: maximum value
        :param points: number of points to display
        :return: 2d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                self.param(functionx, functiony, max_val, min_val, points)

    def plot(self, function, min_val, max_val, points):
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
                self.plot(function, max_val, min_val, points)
            else:
                x_values = linspace(min_val, max_val, points)
                plt.plot(x_values, function(x_values))
                plt.show()


class Plot3d(object):
    """ 3D plot """

    @staticmethod
    def scatter(vectorx, vectory, vectorz):
        """
        :param vectorx: vector in x axis
        :param vectory: vector in y axis
        :param vectorz: vector in z axis
        :return: plot 3d scattered points
        """

        if len(vectorx) == len(vectory) == len(vectorz):
            # general settings
            fig = plt.figure()
            chart = fig.add_subplot(111, projection="3d")

            # plot
            chart.scatter(vectorx, vectory, vectorz, c="r", marker="o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    def param(self, functionx, functiony, functionz, min_val, max_val, points):
        """
        :param functionx: function in x
        :param functiony: function in y
        :param functionz: function in z
        :param min_val: minimum
        :param max_val: maximum
        :param points: number of points
        :return: 3d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min_val > max_val:
                self.param(
                    functionx,
                    functiony,
                    functionz,
                    max_val,
                    min_val,
                    points
                )
            # general settings
            fig = plt.figure()
            chart = fig.gca(projection="3d")

            # limits and plot
            theta = linspace(min_val, max_val, points)

            # z = linspace(-2, 2, 100)
            # r = z**2 + 1
            x_axis = functionx(theta)
            y_axis = functiony(theta)
            z_axis = functionz(theta)
            chart.plot(x_axis, y_axis, z_axis)
            chart.legend()

            # show
            plt.show()

    def plot(self, function, minx, maxx, pointsx, miny, maxy, pointsy):
        """
        :param function: function to plot
        :param minx: minimum of x-values
        :param maxx: maximum of x-values
        :param pointsx: points in x axis
        :param miny: minimum of y-values
        :param maxy: maximum of y-values
        :param pointsy: points in y axis
        :return: plot 3d function
        """
        if pointsx < 0 or pointsy < 0:
            raise ValueError("Number of points to plot must be positive.")

        if minx > maxx:
            self.plot(function, maxx, minx, pointsx, miny, maxy, pointsy)

        if miny > maxy:
            self.plot(function, minx, maxx, pointsx, maxy, miny, pointsy)

        # general settings
        chart = plt.axes(projection="3d")

        # points
        x_axis = numpy.outer(
            linspace(minx, maxx, pointsx), numpy.ones(pointsx)
        )
        y_axis = numpy.outer(
            linspace(miny, maxy, pointsy), numpy.ones(pointsy)
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
    def scatter(vectorx, vectory, vectorz, vectorw):
        """
        :param vectorx: vector in x axis
        :param vectory: vector in y axis
        :param vectorz: vector in z axis
        :param vectorw: vector in w axis
        :return: plot 4d scattered points
        """
        if len(vectorx) == len(vectory) == len(vectorz) == len(vectorw):
            pass
        else:
            raise ValueError("Cannot plot vectors of different length.")

    def plot(self, function, minx, maxx, miny, maxy, minz, maxz, precision,
             kind):
        """
        :param function: function to plot
        :param minx: minimum of x-values
        :param maxx: maximum of x-values
        :param miny: minimum of y-values
        :param maxy: maximum of y-values
        :param minz: minimum of z-values
        :param maxz: maximum of z-values
        :param precision: precision
        :param kind: slice: x cont -> 3d plot with y, z variables in plane
            and w as "z"-axis contour: x cont -> 3d plot with y,z variables in
            plane and w colored
        :return: plot 4d function
        """

        if precision < 0:
            raise ValueError("Precision cannot be negative.")

        if minx > maxx:
            self.plot(function, maxx, minx, miny, maxy, minz, maxz, precision,
                      kind)

        if miny > maxy:
            self.plot(function, minx, maxx, maxy, miny, minz, maxz, precision,
                      kind)

        if minz > maxz:
            self.plot(function, minx, maxx, miny, maxy, maxz, minz, precision,
                      kind)

        if kind != "slice" and kind != "contour":
            raise ValueError(
                "Plot type not supported, only \"slice\" and \"contour\" are.")

        def set_labels(graph, labelx, labely, labelz):
            """
            :param graph: plot
            :param labelx: new label on x axis
            :param labely: new label on y axis
            :param labelz: new label on z axis
            :return: set given labels to axes of graph
            """

            graph.set_xlabel(labelx)
            graph.set_ylabel(labely)
            graph.set_zlabel(labelz)

        def set_limits(graph, min_x, max_x, max_y, min_y, min_z, max_z):
            """
            :param graph: plot
            :param min_x: minimum of x-values
            :param max_x: maximum of x-values
            :param min_y: minimum of y-values
            :param max_y: maximum of y-values
            :param min_z: minimum of z-values
            :param max_z: maximum of z-values
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

        def get_precision_delta(min_val, max_val, prec):
            """
            :param min_val: mnimum
            :param max_val: maximum
            :param prec: precision
            :return: default Delta = interval / points
            """

            return float(max_val - min_val) / float(10 * prec)

        if kind == "slice":
            chart_axis = plt.axes(projection="3d")  # general settings
            pointsx = get_precision(minx, maxx)
            pointsy = get_precision(miny, maxz)

            x_ax = numpy.outer(linspace(minx, maxx, pointsx), pointsx)  # axes
            y_ax = numpy.outer(
                linspace(miny, maxy, pointsy).flatten(), pointsy
            ).T
            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", minx, maxx, valinit=minx)

            def update(val):
                """
                :param val: new value
                :return: re-plot
                """

                chart_axis.clear()
                x_const = slider.val
                z_axis = function(x_const, x_ax, y_ax)
                chart_axis.plot_surface(
                    x_ax, y_ax, z_axis, alpha=0.3, linewidth=2.0
                )
                set_labels(chart_axis, "y", "z", "w")

            slider.on_changed(update)
            set_labels(chart_axis, "y", "z", "w")
            # plot
            plt.show()
        else:  # kind = contour
            # general settings
            fig = plt.figure()
            chart_axis = fig.gca(projection="3d")

            # create axes
            x_ax = numpy.arange(minx, maxx, get_precision_delta(
                minx, maxx, precision)).tolist()
            y_ax = numpy.arange(miny, maxy, get_precision_delta(
                miny, maxy, precision)).tolist()
            x_ax, y_ax = numpy.meshgrid(x_ax, y_ax)

            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", minx, maxx, valinit=minx)

            # update

            def update(val):
                """
                :param val: new value
                :return: re-plot plot
                """

                chart_axis.clear()  # replot
                x_const = slider.val
                z_axis = []

                # add new points
                for i, _ in enumerate(x_ax):
                    z_axis.append(function(x_const, x_ax[i], y_ax[i]))

                # show
                # cset = ax.contour(X, Y, Z, zdir="x", offset=minx)
                # cset = ax.contour(X, Y, Z, zdir="y", offset=miny)
                # cset = ax.contour(X, Y, Z, zdir="z", offset=minz)
                # cset = ax.contour(X, Y, Z, extend3d=True)
                set_labels(chart_axis, "y", "z", "w")

            slider.on_changed(update)
            set_limits(chart_axis, minx, maxx, miny, maxy, minz, maxz)
            plt.show()
