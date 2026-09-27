---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: time certificate of deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'time deposit account that allows deposits evidenced by a negotiable or nonnegotiable instrument, or a deposit
      in book entry form evidenced by a receipt or similar acknowledgement issued by the bank, that provides, on its face,
      that the amount of such deposit is payable to the bearer, to any specified person, or to the order of a specified person,
      as follows: (1) on a certain date not less than seven days after the date of deposit, (2) at the expiration of a specified
      period not less than seven days after the date of the deposit, or (3) upon written notice to the bank which is to be
      given not less than seven days before the date of withdrawal.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CDA
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeCertificateOfDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: time certificate of deposit account
type: Ontology Class
---

# time certificate of deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeCertificateOfDepositAccount>

## Definition

time deposit account that allows deposits evidenced by a negotiable or nonnegotiable instrument, or a deposit in book entry form evidenced by a receipt or similar acknowledgement issued by the bank, that provides, on its face, that the amount of such deposit is payable to the bearer, to any specified person, or to the order of a specified person, as follows: (1) on a certain date not less than seven days after the date of deposit, (2) at the expiration of a specified period not less than seven days after the date of the deposit, or (3) upon written notice to the bank which is to be given not less than seven days before the date of withdrawal.

## Relationships

- **Subclass of**: [TimeDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: some values from of type [CertificateOfDeposit](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit.md)

## Annotations

- **label**: time certificate of deposit account
- **definition**: time deposit account that allows deposits evidenced by a negotiable or nonnegotiable instrument, or a deposit in book entry form evidenced by a receipt or similar acknowledgement issued by the bank, that provides, on its face, that the amount of such deposit is payable to the bearer, to any specified person, or to the order of a specified person, as follows: (1) on a certain date not less than seven days after the date of deposit, (2) at the expiration of a specified period not less than seven days after the date of the deposit, or (3) upon written notice to the bank which is to be given not less than seven days before the date of withdrawal.
- **abbreviation**: CDA

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
