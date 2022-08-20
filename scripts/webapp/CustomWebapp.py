from iml.source.webapp import BaseWebApp
import streamlit as st
import numpy as np
import plotly.graph_objects as go

class CustomWebapp(BaseWebApp):
    nx: int = 11
    ny: int = 11
    pass

    def __init__(self, nx=11, ny=11):
        super().__init__()
        self.nx = nx
        self.ny = ny

    def introduction_section(self):
        pass

    def data_exploration_section(self):
        st.header('Generador de cuadros')
        st.write('Este es un ejemplo de un generador de cuadros')

        points = self.generate_square_points(nx=self.nx,
                                             ny=self.ny,
                                             n_points=2
                                             )
        squares = self.generate_two_squares(points)
        square_plot = self.generate_plotly_plot(squares)



    def training_section(self):
        pass

    def validation_section(self):
        pass


    def generate_square_points(self,
                               n_points,
                               nx=11,
                               ny=11,
                               fix_points=True,
                               ):
        """
        Generate needed points
        """
        points = []
        for i in range(n_points):
            if not fix_points:
                x = np.random.randint(0, nx)
                y = np.random.randint(0, ny)

            else:
                x = np.random.randint(1, nx - 1)
                y = np.random.randint(1, ny - 1)
            points.append([x, y])
        return points

    def generate_two_squares(self, points):
        """
        Generate needed points
        """
        squares = []
        # Square 1
        square_1 = [
            [0, 0],
            points[0],
            points[1],
            [0, self.ny]
        ]
        squares.append(square_1)

        return squares


    def generate_plotly_plot(self, squares):
        pass






