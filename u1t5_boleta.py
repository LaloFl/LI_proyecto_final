def main():
    strs = []
    strs.append("DATOS DE ALUMNO")
    strs.append('           FLORES                   SANDOVAL                DIEGO EDUARDO      ')
    strs.append('     ==================        ==================         =================    ')
    strs.append('      APELLIDO PATERNO          APELLIDO MATERNO              NOMBRE(S)        ')
    strs.append('\nDATOS DE LA ESCUELA                                                            ')
    strs.append('      TECNM CAMPUS TIJUANA          A             VESPERTINO            N/A    ')
    strs.append('    ========================     =======         ============          =====   ')
    strs.append('      NOMBRE DE LA ESCUELA        GRUPO             TURNO               CCT    ')
    strs.append('\n|--------------------------------------------------| |-----------------------| ')
    strs.append('|                 |PERIODOS DE EVALUACION |        | |       ASISTENCIA      | ')
    strs.append('|ASIGNATURAS/AREAS|-----------------------|PROMEDIO| |-----------------------| ')
    strs.append('|                 |  1RO  |  2DO  |  3RO  |        | |CALENDARIO ESCOLAR| 190| ')
    strs.append('|-----------------|--------------------------------| |-----------------------| ')
    strs.append('|   MATEMATICAS   |  9.9  |  9.9  |  9.9  |  9.9   | |    ASISTENCIAS   | 190| ')
    strs.append('|-----------------|--------------------------------| |-----------------------| ')
    strs.append('|     QUIMICA     |  9.9  |  9.9  |  9.9  |  9.9   | | % DE ASISTENCIA  | 100| ')
    strs.append('|-----------------|--------------------------------| |-----------------------| ')
    strs.append('|     HISTORIA    |  9.9  |  9.9  |  9.9  |  9.9   |  *ASISTENCIA MINIMA PARA  ')
    strs.append('|--------------------------------------------------|   SER PROMOVIDO: 80%      ')
    strs.append('\n                                                     |-----------------------| ')
    strs.append('                                                     |PROMEDIO FINAL DE GRADO| ')
    strs.append('  |--------------------|   |--------------------|    |-----------------------| ')
    strs.append('  |  PROMOVIDO   |  X  |   | NO PROMOVIDO |     |    |          9.9          | ')
    strs.append('  |--------------------|   |--------------------|    |-----------------------| ')

    for s in strs:
        print(s)