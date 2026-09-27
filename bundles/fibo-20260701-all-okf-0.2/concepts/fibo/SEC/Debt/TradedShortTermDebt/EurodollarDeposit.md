---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: eurodollar deposit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a certificate of deposit with a fixed interest rate issued in U.S. dollars outside the jurisdiction of the Federal
      Reserve, held at banks outside of the United States, including branches of U.S. banks located outside of the U.S.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A bank in Japan or Singapore may accept dollar deposits, but these are still called Eurodollar deposits. The market
      also includes other currencies, so there are Eurosterling, Euroyen, Euroswiss, etc. Eurocurrency is the general term
      for any currency deposited in bank branches outside countries where it is the national currency.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/EurodollarDeposit
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: eurodollar deposit
type: Ontology Class
---

# eurodollar deposit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/EurodollarDeposit>

## Definition

a certificate of deposit with a fixed interest rate issued in U.S. dollars outside the jurisdiction of the Federal Reserve, held at banks outside of the United States, including branches of U.S. banks located outside of the U.S.

## Relationships

- **Subclass of**: [CertificateOfDeposit](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit.md)

## Annotations

- **label** (en): eurodollar deposit
- **definition** (en): a certificate of deposit with a fixed interest rate issued in U.S. dollars outside the jurisdiction of the Federal Reserve, held at banks outside of the United States, including branches of U.S. banks located outside of the U.S.
- **explanatoryNote** (en): A bank in Japan or Singapore may accept dollar deposits, but these are still called Eurodollar deposits. The market also includes other currencies, so there are Eurosterling, Euroyen, Euroswiss, etc. Eurocurrency is the general term for any currency deposited in bank branches outside countries where it is the national currency.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
