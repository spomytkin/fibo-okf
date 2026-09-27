---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subsidiary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity that is entirely or majority owned and controlled by another legal entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A subsidiary is a separate, distinct legal entity from its parent company(ies) for the purposes of taxation, regulatory
      compliance, and with respect to liability.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Subsidiary
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: subsidiary
type: Ontology Class
---

# subsidiary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Subsidiary>

## Definition

legal entity that is entirely or majority owned and controlled by another legal entity

## Relationships

- **Subclass of**: [ControlledAffiliate](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md)

## Annotations

- **label**: subsidiary
- **definition**: legal entity that is entirely or majority owned and controlled by another legal entity
- **explanatoryNote**: A subsidiary is a separate, distinct legal entity from its parent company(ies) for the purposes of taxation, regulatory compliance, and with respect to liability.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
