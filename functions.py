from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from warnings import filterwarnings
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES
filterwarnings(action='ignore')
def desenha_mapa(address, radius=1000, estilo='Peach', retangular=False):
    aoi = get_aoi(address=address, radius=radius, rectangular=retangular)
    df = get_osm_geometries(aoi=aoi)
    fig = Plot(
        df=df,
        aoi_bounds=aoi.bounds,
        draw_settings=STYLES[estilo]
    ).plot_all()
    fig.savefig('mapa.jpg', dpi=300, bbox_inches='tight')
    return fig