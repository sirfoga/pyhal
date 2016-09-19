# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
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


""" PLOTTER: show elegant plots in any dimension """


from scipy import *
import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import *


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
            fig = plt.figure()
            ax = fig.add_subplot(111)

            # ax.scatter(vectorx, vectory, c="r", marker="o")
            plt.plot(vectorx, vectory, "-o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    def param(self, functionx, functiony, min, max, points):
        """
        :param functionx: function in x value
        :param functiony: function in y value
        ::param min: minimum value
        :param max: maximum value
        :param points: number of points to display
        :return: 2d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min > max:
                self.param(functionx, functiony, max, min, points)
            pass

    def plot(self, function, min, max, points):
        """
        :param function: function to plot
        :param min: minimum value
        :param max: maximum value
        :param points: number of points
        :return: plot 2d function
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min > max:
                self.plot(function, max, min, points)
            else:
                # limits and plot
                x = linspace(min, max, points)
                plt.plot(x, function(x))

                # show
                plt.show()


class Plot3d(object):
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
            ax = fig.add_subplot(111, projection="3d")

            # plot
            ax.scatter(vectorx, vectory, vectorz, c="r", marker="o")
            plt.show()
        else:
            raise ValueError("Cannot plot vectors of different length.")

    def param(self, functionx, functiony, functionz, min, max, points):
        """
        :param functionx: function in x
        :param functiony: function in y
        :param functionz: function in z
        :param min: minimum
        :param max: maximum
        :param points: number of points
        :return: 3d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")
        else:
            if min > max:
                self.param(functionx, functiony, max, min, points)
            else:
                # general settings
                fig = plt.figure()
                ax = fig.gca(projection="3d")

                # limits and plot
                theta = linspace(min, max, points)

                # z = linspace(-2, 2, 100)
                # r = z**2 + 1
                x = functionx(theta)
                y = functiony(theta)
                z = functionz(theta)
                ax.plot(x, y, z)
                ax.legend()

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
        fig = plt.figure()
        ax = plt.axes(projection="3d")

        # points
        x = numpy.outer(linspace(minx, maxx, pointsx), numpy.ones(pointsx))
        y = numpy.outer(linspace(miny, maxy, pointsy), numpy.ones(pointsy)).T
        z = function(x,y)

        # plot
        ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
        plt.show()


class Plot4d(object):
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

    def param(self, functionx, functiony, functionz, functionw, min, max, points):
        """
        :param functionx: function in x
        :param functiony: function in y
        :param functionz: function in z
        :param functionw: function in w
        :param min: minimum
        :param max: maximum
        :param points: number of points
        :return: 4d parametric graph of given function from min to max
        """

        if points < 0:
            raise ValueError("Number of points to plot must be positive.")

        else:
            if min > max:
                self.plot(functionx, functiony, functionz, functionw, max, min, points)
            else:
                pass

    def plot(self, function, minx, maxx, miny, maxy, minz, maxz, precision, kind):
        """
        :param function: function to plot
        :param minx: minimum of x-values
        :param maxx: maximum of x-values
        :param miny: minimum of y-values
        :param maxy: maximum of y-values
        :param minz: minimum of z-values
        :param maxz: maximum of z-values
        :param precision: precision
        :param kind: slice: x cont -> 3d plot with y,z variables in plane and w as "z"-axis
                     contour: x cont -> 3d plot with y,z variables in plane and w colored
        :return: plot 4d function
        """

        if precision < 0:
            raise ValueError("Precision cannot be negative.")

        if minx > maxx:
            self.plot(function, maxx, minx, miny, maxy, minz, maxz, precision, kind)

        if miny > maxy:
            self.plot(function, minx, maxx, maxy, miny, minz, maxz, precision, kind)

        if minz > maxz:
            self.plot(function, minx, maxx, miny, maxy, maxz, minz, precision, kind)

        if kind != "slice" and kind != "contour":
            raise ValueError("Plot type not supported, only \"slice\" and \"contour\" are.")

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

        def set_limits(graph, minx, maxx, maxy, miny, minz, maxz):
            """
            :param graph: plot
            :param minx: minimum of x-values
            :param maxx: maximum of x-values
            :param miny: minimum of y-values
            :param maxy: maximum of y-values
            :param minz: minimum of z-values
            :param maxz: maximum of z-values
            :return: set given limits to axes of graph
            """

            graph.set_xlim(minx, maxx)
            graph.set_ylim(miny, maxy)
            graph.set_zlim(minz, maxz)

        def get_precision(min, max):
            """
            :param min: minimum
            :param max: maximum
            :return: default number of points = interval / 0.1
            """

            return int((max - min) * (1 + precision))

        def get_precision_delta(min, max, precision):
            """
            :param min: mnimum
            :param max: maximum
            :param precision: precision
            :return: default Delta = interval / points
            """

            return float(max - min) / float(10 * precision)

        if kind == "slice":
            # general settings
            fig = plt.figure()
            ax = plt.axes(projection="3d")
            x_const = minx

            # points
            pointsx = get_precision(minx, maxx)
            pointsy = get_precision(miny, maxz)
            pointsz = get_precision(miny, maxz)

            # create axes
            X = numpy.outer(linspace(minx, maxx, pointsx), pointsx)
            Y = numpy.outer(linspace(miny, maxy, pointsy).flatten(), pointsy).T
            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", minx, maxx, valinit=minx)
            # update

            def update(val):
                """
                :param val: new value
                :return: re-plot
                """

                ax.clear()
                x_const = slider.val
                Z = function(x_const, X, Y)
                ax.plot_surface(X, Y, Z, alpha=0.3, linewidth=2.0)
                set_labels(ax, "y", "z", "w")

            slider.on_changed(update)
            set_labels(ax, "y", "z", "w")
            # plot
            plt.show()
        else:  # kind = contour
            # general settings
            fig = plt.figure()
            ax = fig.gca(projection="3d")
            x_const = minx

            # create axes
            X = numpy.arange(minx, maxx, get_precision_delta(minx, maxx, precision)).tolist()
            Y = numpy.arange(miny, maxy, get_precision_delta(miny, maxy, precision)).tolist()
            X, Y = numpy.meshgrid(X, Y)

            # slider
            axis_slider = plt.axes([0.12, 0.03, 0.78, 0.03], axisbg="white")
            slider = Slider(axis_slider, "x", minx, maxx, valinit=minx)

            # update

            def update(val):
                """
                :param val: new value
                :return: re-plot plot
                """

                # replot
                ax.clear()
                x_const = slider.val
                Z = []

                # add new points
                for i in range(len(X)):
                    Z.append(function(x_const, X[i], Y[i]))

                # show
                cset = ax.contour(X, Y, Z, zdir="x", offset=minx)
                cset = ax.contour(X, Y, Z, zdir="y", offset=miny)
                cset = ax.contour(X, Y, Z, zdir="z", offset=minz)
                cset = ax.contour(X, Y, Z, extend3d=True)
                set_labels(ax, "y", "z", "w")

            slider.on_changed(update)
            set_limits(ax, minx, maxx, miny, maxy, minz, maxz)
            plt.show()
