---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: FINRA operating-level market identifier
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: FINR
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarketIdentifier
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/ActiveMICStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasMarketIdentifierCodeStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ActiveMICStatus
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md
    predicate: https://www.omg.org/spec/Commons/Identifiers/identifies
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/MICCodeScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/MICCodeScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/MIC-FINR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: FINRA operating-level market identifier
type: Ontology Individual
---

# FINRA operating-level market identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/MIC-FINR>

## Relationships

- **Related to**: [ActiveMICStatus](/concepts/fibo/FBC/FunctionalEntities/Markets/ActiveMICStatus.md)
- **Related to**: [MICCodeScheme](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/MICCodeScheme.md)
- **Related to**: [Facility-FINR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md)

## Annotations

- **label**: FINRA operating-level market identifier
- **hasTag**: FINR

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
