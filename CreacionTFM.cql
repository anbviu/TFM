CREATE KEYSPACE sistemasopticos
WITH replication = {
	'class' : 'SimpleStrategy',
	'replication_factor' : 1
};

CREATE TABLE sistemasopticos.medidas_por_operador_instrumento_fecha (
	id uuid,
	experimento_operador text,
	experimento_instrumento text,
	experimento_fecha text,
	experimento_fecha_comp timestamp,
	medida_intensidad float,
	medida_parametro float,
	medida_longitud float,
	idexperimento int,
	idmedida int,
	PRIMARY KEY (experimento_operador, experimento_instrumento, experimento_fecha, experimento_fecha_comp,
	medida_parametro, medida_longitud)
);

CREATE TABLE sistemasopticos.medidas_por_fecha (
	id uuid,
	experimento_operador text,
	experimento_fecha text,
	experimento_instrumento text,
	experimento_fecha_comp timestamp,
	medida_intensidad float,
	medida_parametro float,
	medida_longitud float,
	idexperimento int,
	idmedida int,
	PRIMARY KEY (experimento_fecha, experimento_instrumento, experimento_fecha_comp, medida_parametro, medida_longitud)
);

CREATE TABLE sistemasopticos.medidas_por_instrumento_fecha (
	id uuid,
	experimento_operador text,
	experimento_instrumento text,
	experimento_fecha text,
	experimento_fecha_comp timestamp,
	medida_intensidad float,
	medida_parametro float,
	medida_longitud float,
	idexperimento int,
	idmedida int,
	PRIMARY KEY (experimento_instrumento, experimento_fecha, experimento_fecha_comp, medida_parametro, medida_longitud)
);

CREATE TABLE sistemasopticos.medidas_por_operador_fecha (
	id uuid,
	experimento_operador text,
	experimento_fecha text,
	experimento_instrumento text,
	experimento_fecha_comp timestamp,
	medida_intensidad float,
	medida_parametro float,
	medida_longitud float,
	idexperimento int,
	idmedida int,
	PRIMARY KEY (experimento_operador, experimento_fecha, experimento_instrumento, experimento_fecha_comp,
	medida_parametro, medida_longitud)
);


