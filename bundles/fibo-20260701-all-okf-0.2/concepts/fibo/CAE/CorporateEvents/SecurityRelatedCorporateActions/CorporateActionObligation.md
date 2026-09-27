---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporate action obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An obligation related to the holding of a Security.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Delivery of a security. Not defining direction at this level of the model - one party may have an obligation to
      deliver security or to pay; other party may have an obligation to deliver or to pay. Or there may be just one.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Duty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Duty
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateActionObligation
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: corporate action obligation
type: Ontology Class
---

# corporate action obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CorporateActionObligation>

## Definition

An obligation related to the holding of a Security.

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- **Subclass of**: [Duty](/concepts/fibo/FND/Law/LegalCapacity/Duty.md)

## Annotations

- **label** (en): corporate action obligation
- **definition** (en): An obligation related to the holding of a Security.
- **explanatoryNote** (en): Delivery of a security. Not defining direction at this level of the model - one party may have an obligation to deliver security or to pay; other party may have an obligation to deliver or to pay. Or there may be just one.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
