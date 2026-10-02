---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit tradeline
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: report derived from the transaction history of a credit account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A tradeline on a credit report refers to a specific credit account. Tradelines report snapshot details derived
      from a combination of account features and payment history, and are used by credit reporting agencies as inputs to the
      analysis process that determines a party's credit rating.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/isDerivedFrom
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/Report.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditTradeline
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit tradeline
type: Ontology Class
---

# credit tradeline

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditTradeline>

## Definition

report derived from the transaction history of a credit account

## Relationships

- **Subclass of**: [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)

## Constraints

- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: some values from of type [CreditReport](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditReport.md)
- **[isDerivedFrom](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/isDerivedFrom>)**: some values from of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: credit tradeline
- **definition**: report derived from the transaction history of a credit account
- **explanatoryNote**: A tradeline on a credit report refers to a specific credit account. Tradelines report snapshot details derived from a combination of account features and payment history, and are used by credit reporting agencies as inputs to the analysis process that determines a party's credit rating.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
