
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

from __future__ import absolute_import
from __future__ import print_function
from clawpack.clawutil.data import ClawData

probdata = ClawData()
probdata.read('setprob.data', force=True)
print("Parameters: u = %g, beta = %g" % (probdata.u, probdata.beta))

def qtrue(x,t):
    """
    Solução exata dinâmica que se adapta ao domínio do setrun.py
    """
    from numpy import mod, exp, where, logical_and
    import os

    # 1. Descobrir o tamanho do domínio atual (L)
    # O Clawpack salva isso no arquivo claw.data após o setrun

    from clawpack.clawutil.data import ClawData
    clawdata = ClawData()

    # Tenta ler na pasta atual, se não achar, tenta na pasta 'pai'
    if os.path.exists('claw.data'):
        path_data = 'claw.data'
    else:
        # Sobe um nível para encontrar o arquivo na raiz do projeto
        path_data = os.path.abspath(os.path.join(os.getcwd(), '..', 'claw.data'))
    
    clawdata.read(path_data, force=True)

    xlower = clawdata.lower
    xupper = clawdata.upper
    L = xupper - xlower  # Tamanho do domínio

    # 2. Calcular a posição relativa (x0) considerando periodicidade
    x0 = x - probdata.u * t
    x0 = xlower + mod(x0 - xlower, L) 

    # 3. Gerar as ondas (Gaussiana e Pulso)
    # Dica: Se quiser automatizar os centros, podemos usar variáveis aqui também
    q = exp(-probdata.beta * (x0 - 0.75)**2)
    q = where(logical_and(x0 > 0.1, x0 < 0.4), q + 1, q)
    
    return q 

#--------------------------
def setplot(plotdata=None):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 

    if plotdata is None:
        from clawpack.visclaw.data import ClawPlotData
        plotdata = ClawPlotData()

    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='Pressure and Velocity', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = [-.5,1.3]
    plotaxes.title = 'q'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0
    plotitem.plotstyle = '-o'
    plotitem.color = 'b'

    # Plot true solution for comparison:
    def plot_qtrue(current_data):
        from pylab import plot, legend
        x = current_data.x
        t = current_data.t
        q = qtrue(x,t)
        plot(x,q,'r',label='true solution')
        legend()

    plotaxes.afteraxes = plot_qtrue



    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
