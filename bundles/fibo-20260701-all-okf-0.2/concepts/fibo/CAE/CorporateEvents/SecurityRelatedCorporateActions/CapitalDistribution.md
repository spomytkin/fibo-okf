---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital distribution
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that pays shareholders an amount in cash issued from the issuer's capital account
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This action does not result in a reduction of the face value of a share or in a change to the number of shares
      in circulation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CapitalDistribution
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: capital distribution
type: Ontology Class
---

# capital distribution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/CapitalDistribution>

## Definition

corporate action that pays shareholders an amount in cash issued from the issuer's capital account

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Annotations

- **label** (en): capital distribution
- **definition** (en): corporate action that pays shareholders an amount in cash issued from the issuer's capital account
- **explanatoryNote** (en): This action does not result in a reduction of the face value of a share or in a change to the number of shares in circulation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
