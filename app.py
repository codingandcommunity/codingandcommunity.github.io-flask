from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():

    return render_template(
    'index.html',
    landing_mission_statement = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tempus magna at magna auctor hendrerit. Sed a turpis auctor, egestas justo et, volutpat massa. Sed eu finibus odio. In non vestibulum velit. Vivamus a imperdiet leo, in finibus tellus. Morbi accumsan tellus lectus, sed egestas lectus efficitur iaculis. Nullam efficitur vestibulum maximus. Ut imperdiet semper sapien, sed sodales magna sagittis nec. Praesent luctus mauris nunc, quis ultrices odio sollicitudin at. Vestibulum fermentum sem ex, eu cursus leo sodales id.",
    landing_stats_ratio = "1:1",
    landing_stats_studentstaught = "50",
    landing_stats_events = "11",
    landing_ratio_desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tempus magna at magna auctor hendrerit. Sed a turpis auctor, egestas justo et, volutpat massa. Sed eu finibus odio. In non vestibulum velit. Vivamus a imperdiet leo, in finibus tellus. Morbi accumsan tellus",
    landing_studentstaught_desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tempus magna at magna auctor hendrerit. Sed a turpis auctor, egestas justo et, volutpat massa. Sed eu finibus odio. In non vestibulum velit. Vivamus a imperdiet leo, in finibus tellus. Morbi accumsan tellus",
    landing_events_desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tempus magna at magna auctor hendrerit. Sed a turpis auctor, egestas justo et, volutpat massa. Sed eu finibus odio. In non vestibulum velit. Vivamus a imperdiet leo, in finibus tellus. Morbi accumsan tellus"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
