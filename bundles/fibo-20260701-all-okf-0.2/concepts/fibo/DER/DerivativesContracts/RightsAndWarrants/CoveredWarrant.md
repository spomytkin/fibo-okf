---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: covered warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant)
      an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying
      security by a third party that holds as many securities as would be required if all the warrants are exercised
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Covered warrants are very similar to options in that they can be created to allow holders to benefit from either
      rising prices or falling prices, by having both put and call warrants. They can also be created on a wide variety of
      underlying instruments, not just equities and they are fairly standardised and are mostly traded on exchanges. The main
      difference is that warrants tend to have longer maturity dates, typically measured in years instead of months (as with
      options), and are easier to access for individuals as they can be bought and sold in the same way as shares in the stock
      exchange.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In contrast to traditional equity warrants, with covered warrants, no new issuance of common stock occurs if the
      warrant is exercised. The underlying shares of common stock are usually either owned by the issuer of the covered warrants
      or the issuer has a mechanism, such as owning equity warrants for the underlying shares, through which they can obtain
      the shares.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: covered warrant
type: Ontology Class
---

# covered warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CoveredWarrant>

## Definition

warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that holds as many securities as would be required if all the warrants are exercised

## Relationships

- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label** (en): covered warrant
- **definition** (en): warrant that gives the holder the right, but not the obligation, to buy (call warrant) or to sell (put warrant) an underlying asset at a specified price (the strike or exercise price) by a predetermined date, issued without an accompanying security by a third party that holds as many securities as would be required if all the warrants are exercised
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Covered warrants are very similar to options in that they can be created to allow holders to benefit from either rising prices or falling prices, by having both put and call warrants. They can also be created on a wide variety of underlying instruments, not just equities and they are fairly standardised and are mostly traded on exchanges. The main difference is that warrants tend to have longer maturity dates, typically measured in years instead of months (as with options), and are easier to access for individuals as they can be bought and sold in the same way as shares in the stock exchange.
- **explanatoryNote** (en): In contrast to traditional equity warrants, with covered warrants, no new issuance of common stock occurs if the warrant is exercised. The underlying shares of common stock are usually either owned by the issuer of the covered warrants or the issuer has a mechanism, such as owning equity warrants for the underlying shares, through which they can obtain the shares.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
