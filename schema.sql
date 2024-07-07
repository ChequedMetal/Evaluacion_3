/* INSTRUCCIONES PARA EJECUTAR EN EL LABORATORIO DE DUOC*/
/* USAR BASE DE DATOS mysql*/
USE mysql;
/* ACTUALIZAR CONTRASEÑA DE USUARIO ROOT*/
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234567890';
/* CONFIRMAR CAMBIO DE PRIVILEGIOS (CONTRASEÑA) EN LA BASE DE DATOS*/
FLUSH PRIVILEGES;
/* INSTRUCCIONES PARA EJECUTAR EN LA BASE DE DATOS*/
/* CREACIÓN DE UN NUEVO ESQUEMA */
CREATE DATABASE ecommerce_db;
/* USAR BASE DE DATOS ECOMMERCE*/
USE ecommerce_db;

CREATE TABLE pedido (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombres VARCHAR(180) NOT NULL,
    apellido_paterno VARCHAR(180) NOT NULL,
    apellido_materno VARCHAR(180) NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    correo_electronico VARCHAR(254) NOT NULL,
    detalles_envio TEXT NOT NULL
);

