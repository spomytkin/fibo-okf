---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partial redemption with reduction of nominal value action
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action that involves redemption of securities in part before their scheduled final maturity date with
      reduction of the nominal value of the securities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The outstanding amount of securities will be reduced proportionally. May be mandatory or voluntary.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/CorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/PartialRedemptionWithReductionOfNominalValueAction
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: partial redemption with reduction of nominal value action
type: Ontology Class
---

# partial redemption with reduction of nominal value action

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/PartialRedemptionWithReductionOfNominalValueAction>

## Definition

corporate action that involves redemption of securities in part before their scheduled final maturity date with reduction of the nominal value of the securities

## Relationships

- **Subclass of**: [CorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/CorporateAction.md)

## Annotations

- **label** (en): partial redemption with reduction of nominal value action
- **definition** (en): corporate action that involves redemption of securities in part before their scheduled final maturity date with reduction of the nominal value of the securities
- **explanatoryNote** (en): The outstanding amount of securities will be reduced proportionally. May be mandatory or voluntary.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
