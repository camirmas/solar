from vpython import *

"""Visual model of the solar system, utilizing Newton's Gravitational Law."""

def calculate_deviation(observed, expected):
    """Calculates the percent deviation in planet locations."""
    return abs((mag(observed)-mag(expected))/mag(expected)*100)

# constants

G = 6.67408e-11 # Gravitational constant
dt = 100
au = 149597900e3 # astronomical unit, m
conversion = au / (24 * 3600) # au/day -> m/s

# time management

time_range = 62 * 24 * 3600 # seconds between 12/25-2/25 (62 days)
t = 0 # time elapsed

### Planets

# sun
m_sun = 1.989e30
r_sun = 696340000 # radius of sun, m
s_sun = vec(
    -6.603194660112856E-03*au,
    6.043989724696480E-03*au,
    1.041667200986496E-04*au
)
s_sun_final = vec(
    -7.017123377936195E-03*au,
     5.672429511451431E-03*au,
     1.173484130870040E-04*au
)
v_sun = vec(
    -6.881874533998620E-06*conversion,
    -5.694377441162572E-06*conversion,
     2.166033793285782E-07*conversion
)

# planet scaling for easier viewing
scale_factor = 10
r_test = r_sun * scale_factor

# mercury
s_mercury = vec(
    8.913114680709093e-02*au, 
    -4.372419157899412e-01*au, 
    -4.490119216656256e-02*au) # 12/25
s_mercury_final = vec(
    -3.850312265017665E-01*au,
    -1.926006814708216E-01*au,
    1.859066992820886E-02*au) # 2/25
v_mercury = vec(
    2.185141852877879E-02*conversion,
    7.372045148285450E-03*conversion,
    -1.401990385943134E-03*conversion)
r_mercury = r_test
m_mercury = .330e24


# venus
r_venus = r_test
m_venus = 4.87e24
s_venus = vec(
    -5.542779097496149E-01*au,
    -4.655986864429679E-01*au,
    2.523580746577695E-02*au) # 12/25
s_venus_final = vec(
    5.426318315886154E-01*au,
    -4.704547201932487E-01*au,
    -3.813448111774523E-02*au)
v_venus = vec(
    1.304891101840036E-02*conversion,
    -1.542812943586152E-02*conversion,
    -9.648266418927268E-04*conversion)


# earth
r_earth = r_test
# r_earth = 6371000 # radius of earth, m
m_earth = 5.9722e24 # mass of earth, kg
s_earth = vec(
    -6.432564930720717E-02*au,
    9.878384958400993E-01*au,
    6.032515598783565E-05*au)
s_earth_final = vec(
    -9.134415575954500E-01*au,
    4.033038777291573E-01*au,
    9.917860660597218E-05*au)
v_earth = vec(
    -1.745808117294628E-02*conversion,
    -1.085296673766881E-03*conversion,
    -1.397471147541368E-07*conversion)


# mars
r_mars = r_test
m_mars = .642e24
s_mars = vec(
    6.984679242003360E-01*au,
    1.330211951230428E+00*au,
    1.055726692621145E-02*au)
s_mars_final = vec(
    -1.072298827442317E-01*au,
    1.580544766284500E+00*au,
    3.557861048482098E-02*au)
v_mars = vec(
    -1.182832576496634E-02*conversion,
    7.761379167524576E-03*conversion,
    4.529782513085336E-04*conversion)


# jupiter
r_jupiter = r_test
m_jupiter = 1898e24
s_jupiter = vec(
    2.992922263074153E+00*au,
    -4.115952876210287E+00*au,
    -4.988501139322823E-02*au)
s_jupiter_final = vec(
    3.352101393139451E+00*au,
    -3.801327001825503E+00*au,
    -5.922553131465192E-02*au)
v_jupiter = vec(
    6.009296695763082E-03*conversion,
    4.795484796505474E-03*conversion,
    -1.543546721793127E-04*conversion)


# saturn
r_saturn = r_test
m_saturn = 568e24
s_saturn = vec(
    5.453217038160517E+00*au,
    -8.357423201558433E+00*au,
    -7.178682582575581E-02*au)
s_saturn_final = vec(
    5.720427343137351E+00*au,
    -8.164503864316774E+00*au,
    -8.578268533269506E-02*au)
v_saturn = vec(
    4.361109937668995E-03*conversion,
    3.034070080435694E-03*conversion,
    -2.260656042767609E-04*conversion)
    

# uranus
r_uranus = r_test
m_uranus = 86.8e24
s_uranus = vec(
    1.536093386282575E+01*au,
    1.244750867737449E+01*au,
    -1.527725865319626E-01*au)
s_uranus_final = vec(
    1.520448976903749E+01*au,
    1.262468340988623E+01*au,
    -1.500875761465619E-01*au)
v_uranus = vec(
    -2.505190458241792E-03*conversion,
    2.872516306433058E-03*conversion,
    4.296278557535833E-05*conversion)


# neptune
r_neptune = r_test
m_neptune = 102e24
s_neptune = vec(
    2.945017335057748E+01*au,
    -5.247585957567249E+00*au,
    -5.706457269763382E-01*au)
s_neptune_final = vec(
    2.948239806625153E+01*au,
    -5.054711299702682E+00*au,
    -5.753594785865234E-01*au)
v_neptune = vec(
    5.294906303642744E-04*conversion,
    3.108721711486407E-03*conversion,
    -7.627988070832003E-05*conversion)


planet_data = {
    'Sun': [m_sun, r_sun*scale_factor, v_sun, s_sun, color.red, s_sun_final],
    'Mercury': [m_mercury, r_mercury, v_mercury, s_mercury, color.orange, s_mercury_final],
    'Venus': [m_venus, r_venus, v_venus, s_venus, color.green, s_venus_final],
    'Earth': [m_earth, r_earth, v_earth, s_earth, color.blue, s_earth_final],
    'Mars': [m_mars, r_mars, v_mars, s_mars, color.red, s_mars_final],
    'Jupiter': [m_jupiter, r_jupiter, v_jupiter, s_jupiter, color.yellow, s_jupiter_final],
    'Saturn': [m_saturn, r_saturn, v_saturn, s_saturn, color.orange, s_saturn_final],
    'Uranus': [m_uranus, r_uranus, v_uranus, s_uranus, color.purple, s_uranus_final],
    'Neptune': [m_neptune, r_neptune, v_neptune, s_neptune, color.blue, s_neptune_final],
}


planet_objects = {}


for planet, data in planet_data.items():
    planet_obj = sphere(
        radius = data[1], 
        pos=data[3], 
        color=data[4], 
        make_trail=True)
    planet_obj.mass = data[0]
    planet_obj.velocity = data[2]
    planet_obj.final_expected_pos = data[5]
    planet_objects[planet] = planet_obj
    
# sleep(5)

while True:
    rate(1000)
    
    forces = {}
    for name, planet_1 in planet_objects.items():
        for _, planet_2 in planet_objects.items():
            if planet_1 != planet_2:
                r = planet_1.pos-planet_2.pos
                r_hat = -norm(r)
                dist = mag(r) # current distance
                f_planets = G*planet_1.mass*planet_2.mass/dist**2 * r_hat # force of planet_2 on planet_1
                if forces.get(name):
                    forces[name] += f_planets
                else:
                    forces[name] = f_planets

    for name, f_net in forces.items():
        planet = planet_objects[name]
        acceleration = f_net / planet.mass
        planet.velocity += acceleration * dt
        planet.pos += planet.velocity * dt

    t += dt
        
    if time_range - t in range(dt):
        print("2 months (dt=%s)" % dt)

        for name, planet in planet_objects.items():
            print("\n%s:" % name)
            print("Observed:", planet.pos)
            print("Expected:", planet.final_expected_pos)
            deviation = calculate_deviation(planet.pos, planet.final_expected_pos)
            print("Deviation (%):", deviation)
