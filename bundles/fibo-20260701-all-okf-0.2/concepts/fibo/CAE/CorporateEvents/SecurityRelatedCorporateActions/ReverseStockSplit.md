---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reverse stock split
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action involving a decrease in a company's number of outstanding equities without any change in the shareholder's
      equity or the aggregate market value at the time of the split
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Equity price and nominal value are increased accordingly.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: change in nominal value
  disjoint_with:
  - concept: /concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/StockSplit.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/StockSplit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ReverseStockSplit
sources:
- id: fibo-source-690895114a
  resource: references/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
  sha256: 690895114a0787da52d8b7a7d29be50450d25041659e04b33e16f727ba350a92
  title: FIBO source CAE/CorporateEvents/SecurityRelatedCorporateActions.rdf
title: reverse stock split
type: Ontology Class
---

# reverse stock split

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/ReverseStockSplit>

## Definition

corporate action involving a decrease in a company's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Constraints

- **Disjoint with**: [StockSplit](/concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions/StockSplit.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label** (en): reverse stock split
- **definition** (en): corporate action involving a decrease in a company's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split
- **explanatoryNote** (en): Equity price and nominal value are increased accordingly.
- **synonym** (en): change in nominal value

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
