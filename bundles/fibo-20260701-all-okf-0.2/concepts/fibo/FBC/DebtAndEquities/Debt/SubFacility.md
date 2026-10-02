---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sub-facility
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: portion of a credit facility extended to the borrower for some purpose, possibly per some schedule specified in
      the facility
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Each sub-facility may have separate terms, and may be or include individual promissory notes, depending on the
      facility. The amount of associated with the individual sub-facilities sums to the total credit facility amount. Sub-facilities
      may, individually, have a stated purpose, such as to cover inventory, equipment, accounts receivable, working capital,
      letters of credit, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isConstituentOf
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SubFacility
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: sub-facility
type: Ontology Class
---

# sub-facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SubFacility>

## Definition

portion of a credit facility extended to the borrower for some purpose, possibly per some schedule specified in the facility

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isConstituentOf](<https://www.omg.org/spec/Commons/Collections/isConstituentOf>)**: exact qualified cardinality 1 of type [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)

## Annotations

- **label** (en): sub-facility
- **definition** (en): portion of a credit facility extended to the borrower for some purpose, possibly per some schedule specified in the facility
- **explanatoryNote** (en): Each sub-facility may have separate terms, and may be or include individual promissory notes, depending on the facility. The amount of associated with the individual sub-facilities sums to the total credit facility amount. Sub-facilities may, individually, have a stated purpose, such as to cover inventory, equipment, accounts receivable, working capital, letters of credit, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
