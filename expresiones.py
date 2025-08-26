import re

OCR_PATTERNS = {
    "acto_administrativo_nombramiento": [
        re.compile(r"acto\s+administrativo.*nombramiento", re.IGNORECASE),
        re.compile(r"resoluci[oó]n.*nombramiento", re.IGNORECASE),
        re.compile(r"POR LA CUAL SE HACE UN NOMBRAMIENTO", re.IGNORECASE),
        re.compile(r"POR LA CUAL SE REVOCA UN NOMBRAMIENTO", re.IGNORECASE),
        re.compile(r"NOMBRADO", re.IGNORECASE),
        re.compile(r"usted ha", re.IGNORECASE),
        re.compile(r"nombrado", re.IGNORECASE),
        re.compile(r"sus servicios", re.IGNORECASE),
        re.compile(r"CONTINUACION DE LA RESOLUCION", re.IGNORECASE)
    ],
    "oficio_postulacion": [
        re.compile(r"oficio.*postulaci[oó]n", re.IGNORECASE),
        re.compile(r"radicado.*oficio", re.IGNORECASE),
    ],
    "aceptacion_nombramiento": [
        re.compile(r"aceptaci[oó]n.*nombramiento", re.IGNORECASE),
    ],
    "formato_verificacion_requisitos": [
        re.compile(r"formato.*verificaci[oó]n.*requisitos", re.IGNORECASE),
    ],
    "hoja_vida_funcion_publica": [
        # re.compile(r"hoja.*vida.*funci[oó]n.*p[uú]blica", re.IGNORECASE),
        # re.compile(r"HOJADEVIDA", re.IGNORECASE),
        # re.compile(r"HOJA DE VIDA", re.IGNORECASE),
        # re.compile(r"LEY 190 DE 1995", re.IGNORECASE),
        re.compile(r"DOCUMENTOS PRESENTADOS", re.IGNORECASE),
        re.compile(r"PARA SU INGRESO", re.IGNORECASE),
        re.compile(r"INFORMACION PERSONAL", re.IGNORECASE),
        re.compile(r"REFERENCIAS", re.IGNORECASE),
        re.compile(r"Estado civil", re.IGNORECASE),
        re.compile(r"OCUPACION", re.IGNORECASE),
        re.compile(r"FOTOGRAFIA", re.IGNORECASE),
    ],
    "declaracion_bienes_rentas": [
        re.compile(r"declaraci[oó]n.*bienes.*rentas", re.IGNORECASE),
        re.compile(r"DE BIENES Y RENTAS", re.IGNORECASE),
        re.compile(r"PARA MODIFICAR", re.IGNORECASE),
        re.compile(r"RENTAR", re.IGNORECASE),
        re.compile(r"DECLARACI[OÓ]N DE BIENES Y RENTAS", re.IGNORECASE),
        re.compile(r"RENTAR", re.IGNORECASE),
    ],
    "compromiso_libreta_militar": [
        re.compile(r"compromiso.*libreta.*militar", re.IGNORECASE),
    ],
    "libreta_militar_certificacion": [
        re.compile(r"libreta.*militar", re.IGNORECASE),
        re.compile(r"certificaci[oó]n.*militar", re.IGNORECASE),
        re.compile(r"FUERZAS", re.IGNORECASE),
        re.compile(r"MILITAR", re.IGNORECASE),
        re.compile(r"LIBRETA", re.IGNORECASE),
        re.compile(r"LIBRETAS", re.IGNORECASE),
        re.compile(r"TERCER LINEA", re.IGNORECASE),
        re.compile(r"linea", re.IGNORECASE),

    ],
    "documento_identidad": [
        re.compile(r"c[eé]dula.*ciudadan", re.IGNORECASE),
        re.compile(r"documento.*identidad", re.IGNORECASE),
        re.compile(r"cedula", re.IGNORECASE),
        re.compile(r"republica", re.IGNORECASE),
        # re.compile(r"de colombia", re.IGNORECASE),
    ],
    "diploma_bachiller": [
        re.compile(r"diploma.*bachiller", re.IGNORECASE),
    ],
    "certificados_estudios_tecnicos": [
        re.compile(r"certificados?.*t[eé]cnic", re.IGNORECASE),
    ],
    "certificación_seminario": [
        re.compile(r"certificaci[oó]n de seminario", re.IGNORECASE),
        re.compile(r"ASISTIO AL SEMINARIO", re.IGNORECASE),
        re.compile(r"SEMINARIO", re.IGNORECASE),
        re.compile(r"PARTICIPO EN", re.IGNORECASE),
        re.compile(r"SEMINARIO DE", re.IGNORECASE),
        re.compile(r"SEMINARIO NACIONAL", re.IGNORECASE),
        re.compile(r"SEMINARIO INTERNACIONAL", re.IGNORECASE),
        re.compile(r"SEMINARIO DE CAPACITACION", re.IGNORECASE),

        
    ],
    "certificados_estudios_tecnicos_profesionales": [
        re.compile(r"certificados?.*t[eé]cnic.*profes", re.IGNORECASE),
        re.compile(r"Universidad", re.IGNORECASE),
    ],
    "registro_tarjeta_profesional": [
        re.compile(r"(registro|tarjeta).*profesional", re.IGNORECASE),
    ],
    "certificados_experiencia_laboral": [
        re.compile(r"certificados?.*experiencia.*laboral", re.IGNORECASE),
        re.compile(r"encargandose de asuntos laborales", re.IGNORECASE),
        re.compile(r"sus servicios profesionales", re.IGNORECASE),
        re.compile(r"Jefe de Servicios", re.IGNORECASE),
        re.compile(r"prest[oó] sus servicios", re.IGNORECASE),
        re.compile(r"La presente certificación", re.IGNORECASE),
    ],
    "idoneidad": [
        re.compile(r"idoneidad", re.IGNORECASE),
    ],
    "certificado_cuenta_bancaria": [
        re.compile(r"certificado.*cuenta.*bancaria", re.IGNORECASE),
        re.compile(r"BANCO", re.IGNORECASE),
        re.compile(r"CUENTA", re.IGNORECASE),
        re.compile(r"NUMERO DE CUENTA", re.IGNORECASE),
        re.compile(r"CHEQUE", re.IGNORECASE),
        re.compile(r"TIPO DE CUENTA", re.IGNORECASE),
        re.compile(r"CUENTA DE AHORROS", re.IGNORECASE),
        re.compile(r"CUENTA CORRIENTE", re.IGNORECASE),
        re.compile(r"CUENTA EMPRESARIAL", re.IGNORECASE),
        re.compile(r"CONSULTA DE SALDOS DE CUENTA", re.IGNORECASE),
        re.compile(r"DIRECCION GENERAL DE CRED", re.IGNORECASE),
    ],
    "certificado_antecedentes_judiciales": [
        re.compile(r"antecedentes?.*judiciales?", re.IGNORECASE),
        re.compile(r"judiciales", re.IGNORECASE),
        re.compile(r"CIUDADANIA", re.IGNORECASE),
        re.compile(r"DEPARTAMENTO ADMINISTRATIVO", re.IGNORECASE),
        re.compile(r"Certificado Judicial", re.IGNORECASE),
        re.compile(r"El Departamento Administrativo de Seguridad certifica", re.IGNORECASE),
    ],
    "certificado_antecedentes_fiscales": [
        re.compile(r"antecedentes?.*fiscales?", re.IGNORECASE),
        re.compile(r"CIUDADANIA", re.IGNORECASE),
        re.compile(r"JUICIOS FISCALES", re.IGNORECASE),
        re.compile(r"ONTRALORA DELEGADA PARA INVESTIGACIONES", re.IGNORECASE), 
    ],
    "certificado_antecedentes_disciplinarios": [
        re.compile(r"antecedentes?.*disciplinarios?", re.IGNORECASE),
        re.compile(r"dara dde Erlerica", re.IGNORECASE),
        re.compile(r"DISCIPLINARIO", re.IGNORECASE),
        re.compile(r"CIUDADANIA", re.IGNORECASE),
        re.compile(r"CERTIFICADO DE ANTECEDENTES", re.IGNORECASE),
        re.compile(r"CERTIFICADO ORDINARIO", re.IGNORECASE),
        re.compile(r"una vez consultado", re.IGNORECASE),

    ],
    "protocolo_prevencion_violencia_sexual": [
        re.compile(r"protocolo.*violencia.*sexual", re.IGNORECASE),
        re.compile(r"CIUDADANIA", re.IGNORECASE),
    ],
    "declaracion_demanda_alimentos": [
        re.compile(r"declaraci[oó]n.*demanda.*alimentos", re.IGNORECASE),
        re.compile(r"CIUDADANIA", re.IGNORECASE),
        re.compile(r"no tengo conocimiento", re.IGNORECASE),
        re.compile(r"alimentario", re.IGNORECASE),
        re.compile(r"pendientes de car[aá]cter", re.IGNORECASE),

    ],
    "examen_medico_ingreso": [
        re.compile(r"examen.*m[eé]dico.*ingreso", re.IGNORECASE),
        re.compile(r"EXAMEN DE AFILIACION", re.IGNORECASE),
        re.compile(r"TIPO DE EXAMEN", re.IGNORECASE),
        re.compile(r"examen", re.IGNORECASE),
    ],
    "certificado_salud": [
        re.compile(r"certificado.*salud", re.IGNORECASE),
    ],
    "certificación_curso": [
        re.compile(r"Asisti[oó] al", re.IGNORECASE),
        re.compile(r"CURSO", re.IGNORECASE),
        re.compile(r"nUNIVERSIDAD", re.IGNORECASE),
        re.compile(r"FACULTAD", re.IGNORECASE),
        re.compile(r"al CURSO", re.IGNORECASE),
        re.compile(r"intensidad", re.IGNORECASE),
        re.compile(r"horas", re.IGNORECASE),
    ],
    "certificacion_arl": [
        re.compile(r"certificaci[oó]n.*arl", re.IGNORECASE),
    ],
    "formulario_afiliacion_eps": [
        re.compile(r"FORMULARIO ÚNICO DE AFILIACIÓN", re.IGNORECASE),
        re.compile(r"formulario.*afiliaci[oó]n.*eps", re.IGNORECASE),
        re.compile(r"SALUD", re.IGNORECASE),
        re.compile(r"EPS", re.IGNORECASE),
        re.compile(r"FORMULARIO", re.IGNORECASE),
        re.compile(r"AFILIACIÓN", re.IGNORECASE),
        re.compile(r"E.P.S.", re.IGNORECASE),
        re.compile(r"SEGURIDAD SOCIAL", re.IGNORECASE),
    ],
    "formulario_afiliacion_caja_compensacion": [
        re.compile(r"formulario.*caja.*compensaci[oó]n", re.IGNORECASE),
    ],
    "formulario_afiliacion_cesantias": [
        re.compile(r"formulario.*cesant[ií]as", re.IGNORECASE),
        re.compile(r"cesant[ií]as", re.IGNORECASE),
        re.compile(r"solicitud", re.IGNORECASE),
        re.compile(r"FONDOS DE PENSIONES Y CESANTÍAS", re.IGNORECASE),

    ],
    "formato_prepensionados": [
        re.compile(r"formato.*prepensi[oó]nados", re.IGNORECASE),
    ],
    "formato_compromisos_regimenes_especiales": [
        re.compile(r"formato.*compromisos.*reg[ií]menes.*especiales", re.IGNORECASE),
        re.compile(r"COMPROMETO", re.IGNORECASE),
    ],
    "formato_autorizacion_descuento": [
        re.compile(r"formato.*autorizaci[oó]n.*descuento", re.IGNORECASE),
    ],
    "formato_tratamiento_datos": [
        re.compile(r"formato.*tratamiento.*datos", re.IGNORECASE),
    ],
    "formato_declaracion_documentos_autenticos": [
        re.compile(r"formato.*declaraci[oó]n.*documentos?.*aut[eé]nticos?", re.IGNORECASE),
    ],
    "formato_datos_notificacion_afiliacion": [
        re.compile(r"formato.*notificaci[oó]n.*afiliaci[oó]n", re.IGNORECASE),
    ],
    "formato_induccion": [
        re.compile(r"formato.*inducci[oó]n", re.IGNORECASE),
    ],
    "acta_posesion": [
        re.compile(r"acta.*posesi[oó]n", re.IGNORECASE),
        re.compile(r"ACTA DE POSESION", re.IGNORECASE),
        re.compile(r"ACTA", re.IGNORECASE),
    ],
    "acta_de_grado": [
        re.compile(r"ACTA DE GRADO", re.IGNORECASE),
        re.compile(r"acta.*grado", re.IGNORECASE),
        re.compile(r"SESION DE GRADO"),
        re.compile(r"satisfactoriamente con los requisitos", re.IGNORECASE),
        re.compile(r"la Universidad resuelve", re.IGNORECASE),
        re.compile(r"los requisitos legales", re.IGNORECASE),
        re.compile(r"EXAMENES PREPARATORIOS", re.IGNORECASE),
        re.compile(r"Present[oó] y aprob[oó]")
    ],
    "resolucion_vacaciones": [
        re.compile(r"resoluci[oó]n.*vacaciones", re.IGNORECASE),
        re.compile(r"descuente de mis emolumentos", re.IGNORECASE),
        re.compile(r"vacaciones", re.IGNORECASE),
        re.compile(r"prima vacacional", re.IGNORECASE), 
    ],
    "resolucion_licencias": [
        re.compile(r"resoluci[oó]n.*licencias?", re.IGNORECASE),
    ],
    "resolucion_permisos": [
        re.compile(r"resoluci[oó]n.*permisos?", re.IGNORECASE),
    ],
    "resolucion_comisiones": [
        re.compile(r"resoluci[oó]n.*comisiones?", re.IGNORECASE),
    ],
    "resolucion_renuncia": [
        re.compile(r"resoluci[oó]n.*renuncia", re.IGNORECASE),
    ],
    "resolucion_solicitud": [
        re.compile(r"resoluci[oó]n.*solicitud", re.IGNORECASE),
    ],
    "certificado_afp": [
        re.compile(r"certificado.*afp", re.IGNORECASE),
        re.compile(r"pensiones", re.IGNORECASE),
        re.compile(r"FONDO DE PENSIONES", re.IGNORECASE),
        re.compile(r"SOLICITUD DE VINCULACION", re.IGNORECASE),
        re.compile(r"FONDOS DE PENSIONES Y CESANTÍAS", re.IGNORECASE),
    ],
    "oficio_notificacion_nombramiento": [
        re.compile(r"oficio.*notificaci[oó]n.*nombramiento", re.IGNORECASE),
        re.compile(r"NOMBRADO", re.IGNORECASE),
        re.compile(r"usted ha", re.IGNORECASE),
        re.compile(r"nombrado", re.IGNORECASE),
        re.compile(r"sus servicios", re.IGNORECASE),
    ],
    "declaracion_juramentada": [
        re.compile(r"declaraci[oó]n.*juramentada", re.IGNORECASE),
        re.compile(r"DECLARACI[OÓ]N JURAMENTADA", re.IGNORECASE),
        re.compile(r"DECLARACION JURAMENTADA", re.IGNORECASE),
        re.compile(r"declaraci[oó]n", re.IGNORECASE),
    ],
    "documento_identidad_tarjeta_profesional": [
        re.compile(r"documento.*identidad.*tarjeta.*profesional", re.IGNORECASE),
        re.compile(r"PROFESIONAL DE", re.IGNORECASE),
        re.compile(r"TARJETA PROFESIONAL", re.IGNORECASE),
        re.compile(r"Si esta Tarjeta", re.IGNORECASE),
        re.compile(r"es encontrada por favor", re.IGNORECASE),
    ],
    "certificado representación": [
        re.compile(r"otorgo", re.IGNORECASE),
        re.compile(r"representaci[oó]n adelante", re.IGNORECASE),
        re.compile(r"representaci[oó]n", re.IGNORECASE),
        re.compile(r"PODER", re.IGNORECASE),
        re.compile(r"otorgo poder especial", re.IGNORECASE),
    ],
    "certifica": [
        re.compile(r"CERTIFICADO", re.IGNORECASE),
        re.compile(r"INSCRIBIO como", re.IGNORECASE),
        re.compile(r"INSCRIBIR como", re.IGNORECASE),
    ],
}
