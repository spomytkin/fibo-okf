---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: instrumentality
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: organization that serves a public purpose and is closely tied to a government, but is not a government agency
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An instrumentality is a non-governmental agency that acts independently but whose obligations are backed by a government
      because of its role in providing a public service. Many instrumentalities are private companies, and some are chartered
      directly by government. Instrumentalities are subject to a unique set of laws that shape their activities. Certain organizations,
      such as Sallie Mae in the United States, may be considered instrumentalities from some perspectives but not others.
      Sallie Mae's status was changed in 2004, when it was privatized, and since that time it is no longer considered a government-sponsored
      enterprise (GSE).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Government
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isInstrumentOf
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: instrumentality
type: Ontology Class
---

# instrumentality

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality>

## Definition

organization that serves a public purpose and is closely tied to a government, but is not a government agency

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Constraints

- **[isInstrumentOf](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isInstrumentOf.md)**: some values from of type [Government](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Government.md)
- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: min qualified cardinality 0 of type [StatuteLaw](/concepts/fibo/FND/Law/LegalCore/StatuteLaw.md)

## Annotations

- **label**: instrumentality
- **definition**: organization that serves a public purpose and is closely tied to a government, but is not a government agency
- **explanatoryNote**: An instrumentality is a non-governmental agency that acts independently but whose obligations are backed by a government because of its role in providing a public service. Many instrumentalities are private companies, and some are chartered directly by government. Instrumentalities are subject to a unique set of laws that shape their activities. Certain organizations, such as Sallie Mae in the United States, may be considered instrumentalities from some perspectives but not others. Sallie Mae's status was changed in 2004, when it was privatized, and since that time it is no longer considered a government-sponsored enterprise (GSE).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
