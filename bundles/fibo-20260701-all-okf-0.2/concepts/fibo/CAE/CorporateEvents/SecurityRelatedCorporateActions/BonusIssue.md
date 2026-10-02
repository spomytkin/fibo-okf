---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bonus issue
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action in which security holders are awarded additional assets free of payment from the issuer in proportion
      to their holding
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are different taxation rules for the bonus issue compared to the dividend. There could also be a difference
      in the ranking of the shares that are given to what the holder already holds. Dividends are paid from current profits
      and bonus may be from accumulated reserves of the company. A scrip issue is the issue of new shares at no charge pro
      rata to the holder of existing shares.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: capitalisation issue
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: scrip issue
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/BonusIssue
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: bonus issue
type: Ontology Class
---

# bonus issue

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/BonusIssue>

## Definition

corporate action in which security holders are awarded additional assets free of payment from the issuer in proportion to their holding

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): bonus issue
- **definition** (en): corporate action in which security holders are awarded additional assets free of payment from the issuer in proportion to their holding
- **explanatoryNote** (en): There are different taxation rules for the bonus issue compared to the dividend. There could also be a difference in the ranking of the shares that are given to what the holder already holds. Dividends are paid from current profits and bonus may be from accumulated reserves of the company. A scrip issue is the issue of new shares at no charge pro rata to the holder of existing shares.
- **synonym** (en): capitalisation issue
- **synonym** (en): scrip issue

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
