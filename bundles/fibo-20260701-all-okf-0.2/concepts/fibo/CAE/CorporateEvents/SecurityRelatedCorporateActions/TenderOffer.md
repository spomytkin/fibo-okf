---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tender offer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action involving an offer made to shareholders, normally by a third party, requesting them to sell (tender)
      or exchange their equities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: acquisition
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: buyback
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: purchase offer
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: takeover
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TenderOffer
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: tender offer
type: Ontology Class
---

# tender offer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TenderOffer>

## Definition

corporate action involving an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities

## Relationships

- **Subclass of**: [VoluntaryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label** (en): tender offer
- **definition** (en): corporate action involving an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities
- **synonym** (en): acquisition
- **synonym** (en): buyback
- **synonym** (en): purchase offer
- **synonym** (en): takeover

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
