---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: structured warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that is listed on an exchange, offering investors a way to participate in the price performance of an underlying
      asset without buying it directly
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Unlike company-issued warrants, which are tied to corporate fundraising, structured warrants are issued by third-party
      financial institutions such as investment banks or brokers. They can be based on a variety of underlying assets, including
      individual company shares, a basket of shares, or an index.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When structured warrants are exercised, they are typically cash-settled and do not lead to the creation of new
      shares, thus avoiding dilution of existing shareholders. This is in contrast with company-issued stock options, which
      can potentially lead to the issuance of new shares, which might dilute the value for existing shareholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.phillipnova.com.sg/wp-content/uploads/2023/08/Structured-Warrants-Product-Info-Sheet.pdf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/StructuredWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: structured warrant
type: Ontology Class
---

# structured warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/StructuredWarrant>

## Definition

warrant that is listed on an exchange, offering investors a way to participate in the price performance of an underlying asset without buying it directly

## Relationships

- **See also**: [Structured-Warrants-Product-Info-Sheet.pdf](<https://www.phillipnova.com.sg/wp-content/uploads/2023/08/Structured-Warrants-Product-Info-Sheet.pdf>)
- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label** (en): structured warrant
- **definition** (en): warrant that is listed on an exchange, offering investors a way to participate in the price performance of an underlying asset without buying it directly
- **explanatoryNote** (en): Unlike company-issued warrants, which are tied to corporate fundraising, structured warrants are issued by third-party financial institutions such as investment banks or brokers. They can be based on a variety of underlying assets, including individual company shares, a basket of shares, or an index.
- **explanatoryNote** (en): When structured warrants are exercised, they are typically cash-settled and do not lead to the creation of new shares, thus avoiding dilution of existing shareholders. This is in contrast with company-issued stock options, which can potentially lead to the issuance of new shares, which might dilute the value for existing shareholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
