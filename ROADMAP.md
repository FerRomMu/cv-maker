# Etapas del roadmap

## Fase 1 – Infraestructura base
**Objetivo**: Establecer una base de información estructurada, reutilizable y coherente.

- Arquitectura DDD. ✅
- Configuración de entorno (pip-tools, pre-commit, etc.). ✅
- Persistencia de datos de usuario en JSON. ✅
- Template base. ✅
- Generación CV con template base. ✅
- Pruebas unitarias básicas. *(TO DO)*
- Test de arquitectura. *(TO DO)*

## Fase 2 - Orquestación LLM

**Objetivo**: Permitir que el sistema interprete la descripción de un puesto (JD) y determine qué aspectos del perfil son más relevantes.

- Integrar un servicio de LLM OpenSource.
- Análisis de la JD y selección de secciones relevantes del perfil.
- Generación agentica de CV a partir de JD, información de usuario y template.
- Test E2E
- Publicación de MVP.

## Fase 3 - Interacción de usuario

**Objetivo**: Proveer interfaces de usuario para la utilización del software.

- Interfaz CLI.
- Sistema de templates adicionales.
- Interfaz minimalista (Web + Desktop, opcional).

## Fase 4 - Extensibilidad
**Objetivo:** Garantizar la escalabilidad y adopción del proyecto.

- Testeo de compatibilidad con sistemas ATS.
- Generación automatica de CV en múltiples idiomas (con traducción automática LLM)
- Soporte multilenguaje (Interfaz).
- Documentación funcional y técnica completa.
