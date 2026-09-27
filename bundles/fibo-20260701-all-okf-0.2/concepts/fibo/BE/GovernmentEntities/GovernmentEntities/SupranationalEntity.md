---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supranational entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: governmental or non-governmental entity that is established by international law or treaty or incorporated at an
      international level
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 20275:2017, Financial services - Entity legal forms (ELF), First Edition, July 2017.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Kiljunen, Kimmo (2004). The European Constitution in the Making. Centre for European Policy Studies. pp. 21-26.
      ISBN 978-92-9079-493-6
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A supranational union is a supranational polity which lies somewhere between a confederation that is an association
      of states and a federation that is a state. Unlike states in a federal super-state, member states retain ultimate sovereignty,
      although some sovereignty is shared with, or ceded to, the supranational body.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/SupranationalEntity
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: supranational entity
type: Ontology Class
---

# supranational entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/SupranationalEntity>

## Definition

governmental or non-governmental entity that is established by international law or treaty or incorporated at an international level

## Relationships

- **Subclass of**: [Polity](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/Polity.md)

## Constraints

- **[hasSharedSovereigntyOver](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/hasSharedSovereigntyOver.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[isRepresentedBy](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/isRepresentedBy.md)**: some values from of type [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Annotations

- **label**: supranational entity
- **definition**: governmental or non-governmental entity that is established by international law or treaty or incorporated at an international level
- **adaptedFrom**: ISO 20275:2017, Financial services - Entity legal forms (ELF), First Edition, July 2017.
- **adaptedFrom**: Kiljunen, Kimmo (2004). The European Constitution in the Making. Centre for European Policy Studies. pp. 21-26. ISBN 978-92-9079-493-6
- **explanatoryNote**: A supranational union is a supranational polity which lies somewhere between a confederation that is an association of states and a federation that is a state. Unlike states in a federal super-state, member states retain ultimate sovereignty, although some sovereignty is shared with, or ceded to, the supranational body.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
