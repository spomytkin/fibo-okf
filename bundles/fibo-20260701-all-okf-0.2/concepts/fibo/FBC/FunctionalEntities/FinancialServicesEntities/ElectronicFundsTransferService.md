---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: electronic funds transfer service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: service involving any transfer of funds other than a transaction involving a paper instrument, that is initiated
      through an electronic terminal, telephone, or computer and that orders or authorizes a financial institution to debit
      or credit an account
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: EFT services include transfers through automated teller machines, point-of-sale terminals, automated clearinghouse
      systems, telephone bill-payment plans in which periodic or recurring transfers are contemplated, and remote banking
      programs.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: EFT
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: wire transfer service
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.federalreserve.gov/boarddocs/caletters/2008/0807/08-07_attachment.pdf
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ElectronicFundsTransferService
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: electronic funds transfer service
type: Ontology Class
---

# electronic funds transfer service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ElectronicFundsTransferService>

## Definition

service involving any transfer of funds other than a transaction involving a paper instrument, that is initiated through an electronic terminal, telephone, or computer and that orders or authorizes a financial institution to debit or credit an account

## Relationships

- **See also**: [08-07_attachment.pdf](<https://www.federalreserve.gov/boarddocs/caletters/2008/0807/08-07_attachment.pdf>)
- **Subclass of**: [FinancialService](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)

## Annotations

- **label**: electronic funds transfer service
- **definition**: service involving any transfer of funds other than a transaction involving a paper instrument, that is initiated through an electronic terminal, telephone, or computer and that orders or authorizes a financial institution to debit or credit an account
- **example**: EFT services include transfers through automated teller machines, point-of-sale terminals, automated clearinghouse systems, telephone bill-payment plans in which periodic or recurring transfers are contemplated, and remote banking programs.
- **abbreviation**: EFT
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
- **synonym**: wire transfer service

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
