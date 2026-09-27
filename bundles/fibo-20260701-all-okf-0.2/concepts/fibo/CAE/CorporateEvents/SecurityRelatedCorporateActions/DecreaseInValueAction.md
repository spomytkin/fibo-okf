---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: decrease in value action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action resulting in a reduction of face value of a share or the value of fund assets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The number of circulating shares/units remains unchanged. This event may include a cash pay out to holders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/DecreaseInValueAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: decrease in value action
type: Ontology Class
---

# decrease in value action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/DecreaseInValueAction>

## Definition

corporate action resulting in a reduction of face value of a share or the value of fund assets

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): decrease in value action
- **definition** (en): corporate action resulting in a reduction of face value of a share or the value of fund assets
- **explanatoryNote** (en): The number of circulating shares/units remains unchanged. This event may include a cash pay out to holders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
