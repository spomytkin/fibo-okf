---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: requires secondary unit range
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: if true, indicates that an additional qualifier is needed to complete the delivery point description, such as an
      apartment number
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in some cases, such as for lobby or office, if there are multiple secondary units then a range may be
      needed to differentiate between them, even if the range is not always required.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: requires secondary unit range
type: Ontology Property
---

# requires secondary unit range

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange>

## Definition

if true, indicates that an additional qualifier is needed to complete the delivery point description, such as an apartment number

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **See also**: [pub28.pdf](<https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf>)
- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: requires secondary unit range
- **definition**: if true, indicates that an additional qualifier is needed to complete the delivery point description, such as an apartment number
- **explanatoryNote**: Note that in some cases, such as for lobby or office, if there are multiple secondary units then a range may be needed to differentiate between them, even if the range is not always required.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
